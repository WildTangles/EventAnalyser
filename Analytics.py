#ANALYSIS lib

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

# nlep_val = 0            #initialize a string for number of leptons
# LepTmass_val = 0        #lepton min transverse mass
# LepTmassMax_val = 200   #lepton max transverse mass
# TwoLepcharge_val = 1    #2 Leptons: same/diferent charge
# TwoLepflavour_val = 1   #2 Leptons: same/diferent flavour
# InvariantM_val = 0      #invariant mass
# InvariantM2_val = 0     #invariant mass
# Range_val = 0           #range of invariant mass
# st_lepchargecb = 0      #lepton charge
# st_lepflavourcb = 0     #lepton flavour
# st_InvMasscb = 0        #invariant mass of pair
# leppt_val = 25          #lepton momentum
# st_lepptcb = 0          #state of checkbox
# minnjet_val = 0         #initialize integer for min number of jets
# maxnjet_val = 9         #initialize integer for max number of jets
# btagmin_val = 0         #initialise minimum b-jets
# btagmax_val = 9         #initialise maximum b-jets
# st_btagjetcb = 0        #state of checkbox
# minmissE_val = 0        #concerning missing min momentum
# maxmissE_val = 200      #concerning missing max momentum
# percentg_val = 0.5      #percentage of data to analyze, from 0 to 100
# st_lepcb = 0            #state of checkbox: choose number of charged leptons, 1 = checked 0 = unchecked
# st_jetcb = 0            #state of checkbox: choose number of jets
# st_missPcb = 0          #state of checkbox: missing transverse momentum (GeV)

latestThread = None
histograms =[]
pool= None
analysisComplete = False

def run_analysis(_nlep_val, _LepTmass_val, _LepTmassMax_val, _TwoLepcharge_val, _TwoLepflavour_val, _InvariantM_val, _InvariantM2_val, _Range_val, _st_lepchargecb, _st_lepflavourcb, _st_InvMasscb, _leppt_val, _st_lepptcb, _minnjet_val, _maxnjet_val, _btagmin_val, _btagmax_val, _st_btagjetcb, _minmissE_val, _maxmissE_val, _percentg_val, _st_lepcb, _st_jetcb, _st_missPcb):
    """runs the analysis"""

    global analysisComplete
    analysisComplete = False

    selection = []
    global histograms
    
    del histograms[:]

    CustomConfiguration.Job["Fraction"] = _percentg_val/100.0

    histograms.append("n_jets")

    if _st_jetcb ==1: #number of jets
        jetn_chk = CheckFileSuper.CheckNJets(_minnjet_val,
                _maxnjet_val)
        selection.append(jetn_chk)
 
        
        if _st_btagjetcb == 1: #btagging
            btag_chk = CheckFileSuper.CheckBTag(_btagmin_val,
                _btagmax_val,"btag")
            selection.append(btag_chk)
            histograms.append("btag")

    if _minnjet_val<=_maxnjet_val or _maxnjet_val!=0:
               
        histograms.append("jet_pt")
        histograms.append("jet_eta")
        histograms.append("jet_m")

    histograms.append("lep_n")
        
    if _st_lepcb == 0 or _nlep_val !=0:
        histograms.append("lep_pt")
        histograms.append("lep_eta")
        histograms.append("lep_phi")
        histograms.append("lep_E")

    if _st_lepptcb==1:
        AH.lep_num = _leppt_val
            
    if _st_lepcb != 0: #number of leptons
    
        lepn_chk = CheckFileSuper.CheckNLep(_nlep_val)
        selection.append(lepn_chk)
    
        if _nlep_val==1:
            #transverse mass
            checkTMass = CheckFileSuper.CheckTMass(_LepTmass_val,
                _LepTmassMax_val,0,"WtMass")
            selection.append(checkTMass)
            histograms.append("WtMass")
	 
        if _nlep_val==2:
           if _st_lepchargecb!=0: #lepton charge
                if _TwoLepcharge_val==1:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("same",0,1)
                else:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("different",
                        0,1)
                selection.append(twoLepCharge)
            
           if _st_lepflavourcb!=0: #lepton flavour
               if _TwoLepflavour_val==1:
                   twoLepFlavour = CheckFileSuper.CheckLepFlavour("same",0,1)    
               else:
                   twoLepFlavour = CheckFileSuper.CheckLepFlavour("different",
                        0,1)
               selection.append(twoLepFlavour)
               
           if _st_InvMasscb==1: #invariant mass of pair
               invMassCheck = CheckFileSuper.CheckInvMass(_InvariantM_val,
                    _Range_val,0,1,"invMass")
               selection.append(invMassCheck)
               histograms.append("invMass")
               
        if _nlep_val==3:

            subselection =[]
            if _st_lepchargecb!=0: #lepton charge
                if _TwoLepcharge_val==1:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("same",0,1)
                else:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("different",
                        0,1)   
                subselection.append(twoLepCharge)
       
            if _st_lepflavourcb!=0: #lepton flavour
                if _TwoLepflavour_val==1:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour("same",0,1)    
                else:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour("different",
                        0,1)
               
                subselection.append(twoLepFlavour)

            threeLepton = CheckFileSuper.CheckThreeLepton("invMass",
                _InvariantM_val,_Range_val, _LepTmass_val,
                _LepTmassMax_val,"WtMass", subselection)
            selection.append(threeLepton)
            
            histograms.append("WtMass")
            histograms.append("invMass")
            
        if _nlep_val == 4:
            subselection =[]
        
            if _st_lepchargecb!=0: #lepton charge
                if _TwoLepcharge_val==1:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("same",0,1)
                else:
                    twoLepCharge = CheckFileSuper.CheckLepCharge("different",
                        0,1)
                    
                subselection.append(twoLepCharge)
       
            if _st_lepflavourcb!=0: #lepton flavour
                if _TwoLepflavour_val==1:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour("same",
                        0,1)    
                else:
                    twoLepFlavour = CheckFileSuper.CheckLepFlavour(
                        "different",0,1)
                subselection.append(twoLepFlavour)
                
            fourLepton =CheckFileSuper.CheckFourLepton("invMass",
                "invMass2",_InvariantM_val,_InvariantM2_val,
                _Range_val,subselection)

            selection.append(fourLepton)

            histograms.append("invMass")
            histograms.append("invMass2")

    if _minmissE_val<=_maxmissE_val or _maxmissE_val!=0:
        histograms.append("etmiss")

    if _st_missPcb==1: #missing momentum
        missE_chk = CheckFileSuper.CheckEtMiss(_minmissE_val,
            _maxmissE_val)

        selection.append(missE_chk) 
        
    processingDict = CustomConfiguration.Processes



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

    # previousplots=glob.glob('Output/*.gif')
    # for plot in previousplots:
    #     os.remove(plot)

    if not histograms == []:
        NewPlotResults.plot_results(histograms)

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
        
    
class run_thread(threading.Thread):#MARK
    """thread object for running the analysis"""
    
    def __init__(self, params):
        super(run_thread,self).__init__()
        self.params = params

    def run(self):
        # run_analysis(st_jetcb, minnjet_val, maxnjet_val, st_btagjetcb, btagmin_val, btagmax_val, st_lepcb,
        #              nlep_val, st_lepptcb, leppt_val, LepTmass_val, LepTmassMax_val, st_lepchargecb, TwoLepcharge_val,
        #              st_lepflavourcb, TwoLepflavour_val, st_InvMasscb, InvariantM_val, Range_val, InvariantM2_val,
        #              minmissE_val, maxmissE_val, st_missPcb, percentg_val)
        run_analysis(*self.params)
              
runpressed = False
    
def run_a(params):
    """creates an analysis therad"""

    print(params)

    global analysisComplete
    analysisComplete = False
    global latestThread
    latestThread =run_thread(params)
    latestThread.setDaemon(True)
    latestThread.start()

def get_status():
    return analysisComplete

if __name__ == '__main__':
    run_a()