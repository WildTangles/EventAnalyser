from flask import Flask, request, render_template
from Analytics import startRootAnalysis, getRootStatus
import firebase_admin
from collections import OrderedDict
from firebase_admin import credentials, firestore
import glob
import os
import shutil
import time
import base64
import PickleDB

app = Flask(__name__)
db = None
localdb = None

def dictSwapMinMax(dict, min, max):
    if dict[min] > dict[max]:
        dict[min], dict[max] = dict[max], dict[min]    

def imgToStr(img):
    with open(img, "rb") as imgFile:
        return base64.b64encode(imgFile.read())

def strToImg(data, img):    
    with open(img, "wb") as imgFile:        
        imgFile.write(data.decode('base64'))    

def unicodify(data):
    return unicode(data, "utf-8")    

def genKey(oDict):
    rkey = ''
    for key, value in oDict.items():
        rkey += '__{}-{}'.format(str(key), str(value))  
    return rkey  

def getDefaults():
    eventFeatures = OrderedDict({})
    samples = []

    eventFeatures['nlep_val'] = 0           #number of leptons        
    eventFeatures['LepTmass_val'] = 0       #lepton min transverse mass        
    eventFeatures['LepTmassMax_val'] = 200  #lepton max transverse mass
    eventFeatures['InvariantM_val'] = 0     #lepton pair 1 invariant mass
    eventFeatures['InvariantM2_val'] = 0    #lepton pair 2 invariant mass
    eventFeatures['Range_val'] = 0          #lepton pair invariant mass uncertainty
    eventFeatures['leppt_val'] = 25         #lepton min transverse momentum
    eventFeatures['minnjet_val'] = 0        #min number of jets
    eventFeatures['maxnjet_val'] = 9        #max number of jets
    eventFeatures['btagmin_val'] = 0        #min b tag jets
    eventFeatures['btagmax_val'] = 9        #max b tag jets
    eventFeatures['minmissE_val'] = 0       #min missing transverse momentum
    eventFeatures['maxmissE_val'] = 200     #max missing transverse momentum
    eventFeatures['percentg_val'] = 0.5     #fraction of input data 
    eventFeatures['TwoLepcharge_val'] = 1   #lepton same/opp charge
    eventFeatures['TwoLepflavour_val'] = 1  #lepton same/diff flavour
    eventFeatures['st_lepchargecb'] = 0     #state lepton charge feature selection
    eventFeatures['st_lepflavourcb'] = 0    #state lepton flavour feature selection
    eventFeatures['st_InvMasscb'] = 0       #state of invariant mass feature selection
    eventFeatures['st_lepptcb'] = 0         #state of lepton min transverse momentum feature selection
    eventFeatures['st_btagjetcb'] = 0       #state of b tag jets feature selection
    eventFeatures['st_lepcb'] = 0           #state of charged leptons feature selections
    eventFeatures['st_jetcb'] = 0           #state of jets feature seletion
    eventFeatures['st_missPcb'] = 0         #state of missing transverse momentum feature selection  
    eventFeatures['samplesKey'] = ''        #input samples

    return samples, eventFeatures

def getSamplesKey(samples):
    #gen samples key
    samples.sort()
    samplesKey = ''
    for sample in samples:
        samplesKey += '___{}'.format(sample)            

    return sampleskey

def doStuff(samples, eventFeatures):

    dictSwapMinMax(eventFeatures, 'minmissE_val', 'maxmissE_val')        
    dictSwapMinMax(eventFeatures, 'btagmin_val', 'btagmax_val')
    dictSwapMinMax(eventFeatures, 'minnjet_val', 'maxnjet_val')  

    docKey = unicodify(genKey(eventFeatures))        
    imgRef = db.collection(u'imgStore').document(docKey)
    if localdb.isCached(docKey):
        imgStore = imgRef.get()
        for key, value in imgStore.to_dict().iteritems():
            strToImg(value, 'static/histograms/{}'.format(key))        
    else:
        startRootAnalysis(eventFeatures)
        while not getRootStatus():
           pass            
        histDict = {}
        for histogram in glob.glob("static/histograms/*.gif"):                                
            histDict[unicodify(os.path.basename(histogram))] = unicodify(imgToStr(histogram))                                                                
        imgRef.set(histDict)
        localdb.addToCache(docKey)

@app.route('/DataAnalysis6.html', methods= ['GET', 'POST'])
def TTF():
    if request.method == 'POST':
        samples,eventFeatures = getDefaults()
        #
        eventFeatures['percentg_val'] = float(request.form.get("data-percent"))
        #
        eventFeatures['nlep_val'] = int(request.form.get("number-charged-leptons-choice"))  
        #
        eventFeatures['minnjet_val'] = int(request.form.get("min-number-jets-prompt"))
        eventFeatures['maxnjet_val'] = int(request.form.get("max-number-jets-prompt"))
        eventFeatures['st_jetcb'] = 1  
        #
        eventFeatures['leppt_val'] = float(request.form.get("min-charged-lepton-transverse-momentum"))
        eventFeatures['st_lepptcb'] = 1
        #        
        eventFeatures['st_missPcb'] = 1
        eventFeatures['minmissE_val'] = float(request.form.get("min-missing-transverse-momentum-prompt"))
        eventFeatures['maxmissE_val'] = float(request.form.get("max-missing-transverse-momentum-prompt"))
        #
        eventFeatures['btagmin_val'] = int(request.form.get("min-number-b-jets-prompt"))
        eventFeatures['btagmax_val'] = int(request.form.get("max-number-b-jets-prompt"))
        eventFeatures['st_btagjetcb'] = 1
        #
        doStuff(samples, eventFeatures)
        return render_template('DataAnalysis6.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])         
    else:
        return render_template('DataAnalysis6.html', histograms=[])

@app.route('/DataAnalysis5.html', methods = ['GET', 'POST'])
def TTE():
    if request.method == 'POST':
        samples,eventFeatures = getDefaults()
        #
        eventFeatures['percentg_val'] = float(request.form.get("data-percent"))
        #
        eventFeatures['nlep_val'] = int(request.form.get("number-charged-leptons-choice"))  
        #
        eventFeatures['minnjet_val'] = int(request.form.get("min-number-jets-prompt"))
        eventFeatures['maxnjet_val'] = int(request.form.get("max-number-jets-prompt"))
        eventFeatures['st_jetcb'] = 1  
        #
        eventFeatures['leppt_val'] = float(request.form.get("min-charged-lepton-transverse-momentum"))
        eventFeatures['st_lepptcb'] = 1
        #        
        eventFeatures['st_missPcb'] = 1
        eventFeatures['minmissE_val'] = float(request.form.get("min-missing-transverse-momentum-prompt"))
        eventFeatures['maxmissE_val'] = float(request.form.get("max-missing-transverse-momentum-prompt"))
        doStuff(samples, eventFeatures)
        return render_template('DataAnalysis5.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])                
    else:
        return render_template('DataAnalysis5.html', histograms = [])

@app.route('/DataAnalysis4.html', methods = ['GET', 'POST'])
def TTD():
    if request.method == 'POST':
        samples,eventFeatures = getDefaults()
        #
        eventFeatures['percentg_val'] = float(request.form.get("data-percent"))
        #
        eventFeatures['nlep_val'] = int(request.form.get("number-charged-leptons-choice"))  
        #
        eventFeatures['minnjet_val'] = int(request.form.get("min-number-jets-prompt"))
        eventFeatures['maxnjet_val'] = int(request.form.get("max-number-jets-prompt"))
        eventFeatures['st_jetcb'] = 1  
        #
        eventFeatures['leppt_val'] = float(request.form.get("min-charged-lepton-transverse-momentum"))
        eventFeatures['st_lepptcb'] = 1
        #
        doStuff(samples, eventFeatures)
        return render_template('DataAnalysis4.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])                
    else:
        return render_template('DataAnalysis4.html', histograms = [])

@app.route('/DataAnalysis3.html', methods = ['GET', 'POST'])
def TTC():
    if request.method == 'POST':
        samples,eventFeatures = getDefaults()
        #
        eventFeatures['percentg_val'] = float(request.form.get("data-percent"))
        #
        eventFeatures['nlep_val'] = int(request.form.get("number-charged-leptons-choice"))  
        #
        eventFeatures['minnjet_val'] = int(request.form.get("min-number-jets-prompt"))
        eventFeatures['maxnjet_val'] = int(request.form.get("max-number-jets-prompt"))
        eventFeatures['st_jetcb'] = 1          
        #
        doStuff(samples, eventFeatures)        
        return render_template('DataAnalysis3.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])                
    else:
        return render_template('DataAnalysis3.html', histograms = [])

@app.route('/DataAnalysis2.html', methods = ['GET', 'POST'])
def TTB():
    if request.method == 'POST':
        samples,eventFeatures = getDefaults()
        eventFeatures['percentg_val'] = float(request.form.get("data-percent"))
        eventFeatures['nlep_val'] = int(request.form.get("number-charged-leptons-choice"))            
        doStuff(samples, eventFeatures)        
        return render_template('DataAnalysis2.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])        
    else:
        return render_template('DataAnalysis2.html', histograms = [])

@app.route('/DataAnalysistt.html', methods = ['GET', 'POST'])
def TTA():    
    if request.method == 'POST':
        #get defaults
        samples, eventFeatures = getDefaults()        
        #update params
        eventFeatures['percentg_val'] = float(request.form.get("data-percent"))
        #do stuff
        doStuff(samples, eventFeatures)

        return render_template('DataAnalysistt.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])        
    else:
        return render_template('DataAnalysistt.html', histograms=[])        

@app.route('/introData', methods = ['GET', 'POST'])
def introData():
        if request.method == 'POST':
            return render_template('introData.html', histograms=[placeholder+'?no-cache-token={}'.format(time.time()) for placeholder in glob.glob("static/placeholders/*.gif")])
        else:
            return render_template('introData.html', histograms=[placeholder+'?no-cache-token={}'.format(time.time()) for placeholder in glob.glob("static/placeholders/*.gif")])        

@app.route('/demo', methods = ['GET', 'POST'])
def demo():
    if request.method == 'POST':

        #### defaults ####
        eventFeatures = OrderedDict({})
        eventFeatures['nlep_val'] = 0           #number of leptons        
        eventFeatures['LepTmass_val'] = 0       #lepton min transverse mass        
        eventFeatures['LepTmassMax_val'] = 200  #lepton max transverse mass
        eventFeatures['InvariantM_val'] = 0     #lepton pair 1 invariant mass
        eventFeatures['InvariantM2_val'] = 0    #lepton pair 2 invariant mass
        eventFeatures['Range_val'] = 0          #lepton pair invariant mass uncertainty
        eventFeatures['leppt_val'] = 25         #lepton min transverse momentum
        eventFeatures['minnjet_val'] = 0        #min number of jets
        eventFeatures['maxnjet_val'] = 9        #max number of jets
        eventFeatures['btagmin_val'] = 0        #min b tag jets
        eventFeatures['btagmax_val'] = 9        #max b tag jets
        eventFeatures['minmissE_val'] = 0       #min missing transverse momentum
        eventFeatures['maxmissE_val'] = 200     #max missing transverse momentum
        eventFeatures['percentg_val'] = 0.5     #fraction of input data 
        eventFeatures['TwoLepcharge_val'] = 1   #lepton same/opp charge
        eventFeatures['TwoLepflavour_val'] = 1  #lepton same/diff flavour
        eventFeatures['st_lepchargecb'] = 0     #state lepton charge feature selection
        eventFeatures['st_lepflavourcb'] = 0    #state lepton flavour feature selection
        eventFeatures['st_InvMasscb'] = 0       #state of invariant mass feature selection
        eventFeatures['st_lepptcb'] = 0         #state of lepton min transverse momentum feature selection
        eventFeatures['st_btagjetcb'] = 0       #state of b tag jets feature selection
        eventFeatures['st_lepcb'] = 0           #state of charged leptons feature selections
        eventFeatures['st_jetcb'] = 0           #state of jets feature seletion
        eventFeatures['st_missPcb'] = 0         #state of missing transverse momentum feature selection 
        #### defaults ####

        #### requested ####        
        eventFeatures['percentg_val'] = float(request.form.get("data-percent"))

        if request.form.get("number-charged-leptons-prompts-charge-same"):
            eventFeatures['TwoLepcharge_val'] = 1 
            eventFeatures['st_lepchargecb'] = 1           
        elif request.form.get("number-charged-leptons-prompts-charge-opp"):
            eventFeatures['TwoLepcharge_val'] = -1        
            eventFeatures['st_lepchargecb'] = 1

        if request.form.get("number-charged-leptons-prompts-flavor-same"):
            eventFeatures['TwoLepflavour_val'] = 1
            eventFeatures['st_lepflavourcb'] = 1
        elif request.form.get("number-charged-leptons-prompts-flavor-diff"):
            eventFeatures['TwoLepflavour_val'] = -1
            eventFeatures['st_lepflavourcb'] = 1

        if request.form.get("min-charged-lepton-transverse-momentum-checkbox"):
            eventFeatures['leppt_val'] = float(request.form.get("min-charged-lepton-transverse-momentum"))
            eventFeatures['st_lepptcb'] = 1

        if request.form.get("number-b-jets-checkbox"):
            eventFeatures['btagmin_val'] = int(request.form.get("min-number-b-jets-prompt"))
            eventFeatures['btagmax_val'] = int(request.form.get("max-number-b-jets-prompt"))
            eventFeatures['st_btagjetcb'] = 1
        
        if request.form.get("number-jets-checkbox"):
            eventFeatures['minnjet_val'] = int(request.form.get("min-number-jets-prompt"))
            eventFeatures['maxnjet_val'] = int(request.form.get("max-number-jets-prompt"))
            eventFeatures['st_jetcb'] = 1

        if request.form.get("missing-transverse-momentum-checkbox"):
            eventFeatures['st_missPcb'] = 1
            eventFeatures['minmissE_val'] = float(request.form.get("min-missing-transverse-momentum-prompt"))
            eventFeatures['maxmissE_val'] = float(request.form.get("max-missing-transverse-momentum-prompt"))
                
        if request.form.get("number-charged-leptons"):
            eventFeatures['st_lepcb'] = 1
            eventFeatures['nlep_val'] = int(request.form.get("number-charged-leptons-choice"))            
            if eventFeatures['nlep_val'] == 1:
                eventFeatures['LepTmass_val'] = float(request.form.get("min-number-charged-leptons-prompts-transverse-mass"))               
                eventFeatures['LepTmassMax_val'] = float(request.form.get("max-number-charged-leptons-prompts-transverse-mass"))
            elif eventFeatures['nlep_val'] == 2:
                eventFeatures['InvariantM_val'] = float(request.form.get("val-number-charged-leptons-prompts-invariant-mass1"))
                eventFeatures['Range_val'] = float(request.form.get("unc-number-charged-leptons-prompts-invariant-mass1"))               
                eventFeatures['st_InvMasscb'] = 1
            elif eventFeatures['nlep_val'] == 3:
                eventFeatures['LepTmass_val'] = float(request.form.get("min-number-charged-leptons-prompts-transverse-mass"))               
                eventFeatures['LepTmassMax_val'] = float(request.form.get("max-number-charged-leptons-prompts-transverse-mass"))
            elif eventFeatures['nlep_val'] == 4:
                eventFeatures['InvariantM_val'] = float(request.form.get("val-number-charged-leptons-prompts-invariant-mass1"))
                eventFeatures['Range_val'] = float(request.form.get("unc-number-charged-leptons-prompts-invariant-mass1"))      
                eventFeatures['InvariantM2_val'] = float(request.form.get("val-number-charged-leptons-prompts-invariant-mass2"))                   
        
        dictSwapMinMax(eventFeatures, 'minmissE_val', 'maxmissE_val')        
        dictSwapMinMax(eventFeatures, 'btagmin_val', 'btagmax_val')
        dictSwapMinMax(eventFeatures, 'minnjet_val', 'maxnjet_val')            
        #### requested ####

        #### TMP SAMPLES MANUAL ####
        samples = []
        #example samples to provide
        #samples = [ "data_Egamma", "data_Muons" ]        
        #samples = [ "WW", "ZZ" ]
        #samples = ["data_Egamma", "data_Muons", "Zee", "Zmumu", "Ztautau"]
        #samples = ["data_Egamma", "data_Muons", "WenuJetsBVeto", "WenuWithB", "WenuNoJetsBVeto", "WmunuJetsBVeto", "WmunuWithB", "WmunuNoJetsBVeto", "WtaunuJetsBVeto", "WtaunuWithB", "WtaunuNoJetsBVeto"]
        #samples = ["data_Egamma", "data_Muons", "Zee"]
        #samples = ["ZPrime1000", "ZPrime500", "ZPrime3000"]
        #samples = ["ZPrime1000"]
        #samples = ["data_Egamma", "data_Muons", "Zee", "ZPrime1000"]

        #gen samples key
        samples.sort()
        samplesKey = ''
        for sample in samples:
            samplesKey += '___{}'.format(sample)            
        #

        eventFeatures['samplesKey'] = samplesKey 
        #### TMP SAMPLES MANUAL ####


        docKey = unicodify(genKey(eventFeatures))        
        imgRef = db.collection(u'imgStore').document(docKey)
        if localdb.isCached(docKey):
            imgStore = imgRef.get()
            for key, value in imgStore.to_dict().iteritems():
                strToImg(value, 'static/histograms/{}'.format(key))        
            return render_template('histogramPOST.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")],
                placeholders=[placeholder+'?no-cache-token={}'.format(time.time()) for placeholder in glob.glob("static/placeholders/*.gif")])            
        else:
            startRootAnalysis(eventFeatures)
            while not getRootStatus():
               pass            
            histDict = {}
            for histogram in glob.glob("static/histograms/*.gif"):                                
                histDict[unicodify(os.path.basename(histogram))] = unicodify(imgToStr(histogram))                                                                
            imgRef.set(histDict)
            localdb.addToCache(docKey)
            return render_template('histogramPOST.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")],
                placeholders=[placeholder+'?no-cache-token={}'.format(time.time()) for placeholder in glob.glob("static/placeholders/*.gif")])
            

    else:        
        return render_template('histogramGET.html', placeholders=[placeholder+'?no-cache-token={}'.format(time.time()) for placeholder in glob.glob("static/placeholders/*.gif")])

if __name__ == '__main__':
    cred = credentials.Certificate('atlasopendata-privatekey.json')
    firebase_admin.initialize_app(cred)    
    db = firestore.client()
    localdb = PickleDB.pickleDB('local-db.pickle')
    localdb.loadDB()

    app.run(debug=True)