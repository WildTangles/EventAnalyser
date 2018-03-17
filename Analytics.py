import ROOT
import threading
import CheckFileSuper
import NewRunScript
import NewPlotResults
import NewAnalysisHelpers as AH
import glob
import os
import CustomConfiguration
import NewJob
import multiprocessing
import shutil

pool= None
latestThread = None
histograms =[]
analysisComplete = False

def rootAnalysis(samples, **kwargs):
    """runs the analysis"""

    global analysisComplete
    analysisComplete = False

    selection = []
    global histograms
    
    del histograms[:]

    CustomConfiguration.Job["Fraction"] = kwargs['percentg_val']/100.0

    histograms.append("n_jets")

    if kwargs['st_jetcb'] ==1: #number of jets
        jetn_chk = CheckFileSuper.CheckNJets(kwargs['minnjet_val'],
                kwargs['maxnjet_val'])
        selection.append(jetn_chk)
 
        
        if kwargs['st_btagjetcb'] == 1: #btagging
            btag_chk = CheckFileSuper.CheckBTag(kwargs['btagmin_val'],
                kwargs['btagmax_val'],"btag")
            selection.append(btag_chk)
            histograms.append("btag")

    if kwargs['minnjet_val']<=kwargs['maxnjet_val'] or kwargs['maxnjet_val']!=0:
               
        histograms.append("jet_pt")
        histograms.append("jet_eta")
        histograms.append("jet_m")

    histograms.append("lep_n")
        
    if kwargs['st_lepcb'] == 0 or kwargs['nlep_val']  !=0:
        histograms.append("lep_pt")
        histograms.append("lep_eta")
        histograms.append("lep_phi")
        histograms.append("lep_E")

    if kwargs['st_lepptcb']==1:
        AH.lep_num = kwargs['leppt_val']
            
    if kwargs['st_lepcb'] != 0: #number of leptons
    
        lepn_chk = CheckFileSuper.CheckNLep(kwargs['nlep_val'] )
        selection.append(lepn_chk)
    
        if kwargs['nlep_val'] ==1:
            #transverse mass
            checkTMass = CheckFileSuper.CheckTMass(kwargs['LepTmass_val'],
                kwargs['LepTmassMax_val'],0,"WtMass")
            selection.append(checkTMass)
            histograms.append("WtMass")
	 
        if kwargs['nlep_val'] ==2:
           if kwargs['st_lepchargecb']!=0: #lepton charge
                if kwargs['TwoLepcharge_val']==1:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("same",0,1)
                else:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("different",
                        0,1)
                selection.append(twoLepCharge)
            
           if kwargs['st_lepflavourcb']!=0: #lepton flavour
               if kwargs['TwoLepflavour_val']==1:
                   twoLepFlavour = CheckFileSuper.CheckLepFlavour("same",0,1)    
               else:
                   twoLepFlavour = CheckFileSuper.CheckLepFlavour("different",
                        0,1)
               selection.append(twoLepFlavour)
               
           if kwargs['st_InvMasscb']==1: #invariant mass of pair
               invMassCheck = CheckFileSuper.CheckInvMass(kwargs['InvariantM_val'],
                    kwargs['Range_val'],0,1,"invMass")
               selection.append(invMassCheck)
               histograms.append("invMass")
               
        if kwargs['nlep_val'] ==3:

            subselection =[]
            if kwargs['st_lepchargecb']!=0: #lepton charge
                if kwargs['TwoLepcharge_val']==1:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("same",0,1)
                else:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("different",
                        0,1)   
                subselection.append(twoLepCharge)
       
            if kwargs['st_lepflavourcb']!=0: #lepton flavour
                if kwargs['TwoLepflavour_val']==1:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour("same",0,1)    
                else:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour("different",
                        0,1)
               
                subselection.append(twoLepFlavour)

            threeLepton = CheckFileSuper.CheckThreeLepton("invMass",
                kwargs['InvariantM_val'],kwargs['Range_val'], kwargs['LepTmass_val'],
                kwargs['LepTmassMax_val'],"WtMass", subselection)
            selection.append(threeLepton)
            
            histograms.append("WtMass")
            histograms.append("invMass")
            
        if kwargs['nlep_val']  == 4:
            subselection =[]
        
            if kwargs['st_lepchargecb']!=0: #lepton charge
                if kwargs['TwoLepcharge_val']==1:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("same",0,1)
                else:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("different",
                        0,1)
                    
                subselection.append(twoLepCharge)
       
            if kwargs['st_lepflavourcb']!=0: #lepton flavour
                if kwargs['TwoLepflavour_val']==1:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour("same",
                        0,1)    
                else:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour(
                        "different",0,1)
                subselection.append(twoLepFlavour)
                
            fourLepton =CheckFileSuper.CheckFourLepton("invMass",
                "invMass2",kwargs['InvariantM_val'],kwargs['InvariantM2_val'],
                kwargs['Range_val'],subselection)

            selection.append(fourLepton)

            histograms.append("invMass")
            histograms.append("invMass2")

    if kwargs['minmissE_val']<=kwargs['maxmissE_val'] or kwargs['maxmissE_val']!=0:
        histograms.append("etmiss")

    if kwargs['st_missPcb']==1: #missing momentum
        missE_chk = CheckFileSuper.CheckEtMiss(kwargs['minmissE_val'],
            kwargs['maxmissE_val'])

        selection.append(missE_chk)             

    if samples:        
        processingDict = {}
        for sample in samples:
            processingDict[sample] = CustomConfiguration.Processes[sample]            
    else:        
        processingDict = CustomConfiguration.Processes        

    for oldRootResult in glob.glob("results/*.root"):
        os.remove(oldRootResult)

    CustomConfiguration.Job["Batch"] = True
    jobs = [NewJob.NewJob(processName,CustomConfiguration.Job,
        fileLocation,selection,histograms) for processName, 
        fileLocation in processingDict.items()]
    jobs = NewRunScript.SortJobsBySize(jobs)
    global pool
    pool = []
    for job in jobs:
        process = JobPool(job)
        process
        process.start()
        pool.append(process)
                
    pool.reverse()
    for process in pool:
        process.join()
        #update progress, max = 29

    for oldHistogram in glob.glob("static/histograms/*.gif"):
        os.remove(oldHistogram)
    for oldHistogram in glob.glob("Output/*.gif"):
        os.remove(oldHistogram)

    if histograms:
        NewPlotResults.plot_results(samples,histograms)

    for histogram in glob.glob("Output/*.gif"):
        shutil.copy(histogram, 'static/histograms')


    analysisComplete = True
    
class JobPool(multiprocessing.Process):
    """Process object for running a job"""
    def __init__(self,job):
        super(JobPool,self).__init__()
        self.job = job
    
    def run(self):
        self.job.run()
        
    
class runThread(threading.Thread):#MARK
    """thread object for running the analysis"""
    
    def __init__(self, samples, params):
        super(runThread,self).__init__()
        self.params = params
        self.samples = samples

    def run(self):        
        rootAnalysis(self.samples, **self.params)              
    
def startRootAnalysis(params, samples=None):
    """creates an analysis therad"""

    global analysisComplete
    analysisComplete = False
    global latestThread
    latestThread =runThread(samples, params)
    #latestThread.setDaemon(True)
    latestThread.setDaemon(False)
    latestThread.start()

def getRootStatus():
    return analysisComplete

if __name__ == '__main__':

    testParams = {
        'st_jetcb': 0,
        'minnjet_val': 0,
        'maxnjet_val': 9,
        'st_btagjetcb': 0,
        'btagmin_val': 0,
        'btagmax_val': 9,
        'st_lepcb': 1,
        'nlep_val': 1,
        'st_lepptcb': 0,
        'leppt_val': 25,
        'LepTmass_val': 0,
        'LepTmassMax_val': 200,
        'st_lepchargecb': 0,
        'TwoLepcharge_val': 1,
        'st_lepflavourcb': 0,
        'TwoLepflavour_val': 1,
        'st_InvMasscb': 0,
        'InvariantM_val': 0,
        'Range_val': 0,
        'InvariantM2_val': 0,
        'minmissE_val': 0,
        'maxmissE_val': 200,
        'st_missPcb': 0,
        'percentg_val': 1.0
    }




    # # #testParams to somewhat isolate Z-Prime signal
    # testParams = {
    #     'st_jetcb': 1,
    #     'minnjet_val': 4,
    #     'maxnjet_val': 9,
    #     'st_btagjetcb': 1,
    #     'btagmin_val': 1,
    #     'btagmax_val': 9,
    #     'st_lepcb': 1,
    #     'nlep_val': 1,
    #     'st_lepptcb': 0,
    #     'leppt_val': 25,
    #     'LepTmass_val': 30,
    #     'LepTmassMax_val': 200,
    #     'st_lepchargecb': 0,
    #     'TwoLepcharge_val': 1,
    #     'st_lepflavourcb': 0,
    #     'TwoLepflavour_val': 1,
    #     'st_InvMasscb': 0,
    #     'InvariantM_val': 0,
    #     'Range_val': 0,
    #     'InvariantM2_val': 0,
    #     'minmissE_val': 30,
    #     'maxmissE_val': 200,
    #     'st_missPcb': 0,
    #     'percentg_val': 10.0
    # }

    # descriptor definitions
    # eventFeatures['nlep_val'] = 0           #number of leptons        
    # eventFeatures['LepTmass_val'] = 0       #lepton min transverse mass        
    # eventFeatures['LepTmassMax_val'] = 200  #lepton max transverse mass
    # eventFeatures['InvariantM_val'] = 0     #lepton pair 1 invariant mass
    # eventFeatures['InvariantM2_val'] = 0    #lepton pair 2 invariant mass
    # eventFeatures['Range_val'] = 0          #lepton pair invariant mass uncertainty
    # eventFeatures['leppt_val'] = 25         #lepton min transverse momentum
    # eventFeatures['minnjet_val'] = 0        #min number of jets
    # eventFeatures['maxnjet_val'] = 9        #max number of jets
    # eventFeatures['btagmin_val'] = 0        #min b tag jets
    # eventFeatures['btagmax_val'] = 9        #max b tag jets
    # eventFeatures['minmissE_val'] = 0       #min missing transverse momentum
    # eventFeatures['maxmissE_val'] = 200     #max missing transverse momentum
    # eventFeatures['percentg_val'] = 0.5     #fraction of input data 
    # eventFeatures['TwoLepcharge_val'] = 1   #lepton same/opp charge
    # eventFeatures['TwoLepflavour_val'] = 1  #lepton same/diff flavour
    # eventFeatures['st_lepchargecb'] = 0     #state lepton charge feature selection
    # eventFeatures['st_lepflavourcb'] = 0    #state lepton flavour feature selection
    # eventFeatures['st_InvMasscb'] = 0       #state of invariant mass feature selection
    # eventFeatures['st_lepptcb'] = 0         #state of lepton min transverse momentum feature selection
    # eventFeatures['st_btagjetcb'] = 0       #state of b tag jets feature selection
    # eventFeatures['st_lepcb'] = 0           #state of charged leptons feature selections
    # eventFeatures['st_jetcb'] = 0           #state of jets feature seletion
    # eventFeatures['st_missPcb'] = 0         #state of missing transverse momentum feature selection  
    # eventFeatures['samplesKey'] = ''        #input samples




    #samples = [ "data_Egamma", "data_Muons" ]        
    #samples = [ "WW", "ZZ" ]
    #samples = ["data_Egamma", "data_Muons", "Zee", "Zmumu", "Ztautau"]
    #samples = ["data_Egamma", "data_Muons", "WenuJetsBVeto", "WenuWithB", "WenuNoJetsBVeto", "WmunuJetsBVeto", "WmunuWithB", "WmunuNoJetsBVeto", "WtaunuJetsBVeto", "WtaunuWithB", "WtaunuNoJetsBVeto"]
    #samples = ["data_Egamma", "data_Muons", "Zee"]
    #samples = ["ZPrime1000", "ZPrime500", "ZPrime3000"]
    #samples = ["ZPrime1000"]
    #samples = ["data_Egamma", "data_Muons", "Zee", "ZPrime1000"]
    samples = []   


    startRootAnalysis(testParams, samples)    
