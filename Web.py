from flask import Flask, request, render_template
from Analytics import startRootAnalysis, getRootStatus
import glob
import os
import shutil
import time

app = Flask(__name__)

def dictSwapMinMax(dict, min, max):
    if dict[min] > dict[max]:
        dict[min], dict[max] = dict[max], dict[min]    

@app.route('/')
def whatisthis():
    return render_template('whatisthis.html')

@app.route('/analytics', methods = ['GET', 'POST'])
def analytics():
    if request.method == 'POST':
        params = [ float(param_string) for param_string in request.form.getlist('cut[]') ]
        print(params[-4])
        #params = [0, 0, 200, 1, 1, 0, 0, 0, 0, 0, 0, 25, 0, 0, 9, 0, 9, 0, 0, 200, float(request.form.getlist('cut[]')[0]), 0, 0, 0]
        for oldHistogram in glob.glob("static/histograms/*.gif"):
            os.remove(oldHistogram)
        for oldHistogram in glob.glob("Output/*.gif"):
            os.remove(oldHistogram)
        run_a(params)
        while not getRootStatus():
            pass
        return render_template('analytics.html', histograms=[histogram+'?no-cache-token={}'.format(time.time()) for histogram in glob.glob("static/histograms/*.gif")])
    else:
        return render_template('analytics.html', histograms=[])

@app.route('/histogram', methods = ['GET', 'POST'])
def histogram():
    if request.method == 'POST':

        #### defaults ####
        eventFeatures = {}
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

        for oldHistogram in glob.glob("static/histograms/*.gif"):
            os.remove(oldHistogram)
        for oldHistogram in glob.glob("Output/*.gif"):
            os.remove(oldHistogram)

        startRootAnalysis(eventFeatures)
        print('started')
        while not getRootStatus():            
            pass
        print('done')
        #### requested ####

        return render_template('histogram.html')
    else:
        return render_template('histogram.html')

if __name__ == '__main__':
    app.run(debug=True)