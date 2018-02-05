import ROOT
import threading
import CheckFileSuper
import NewRunScript
import NewPlotResults
import NewAnalysisHelpers as AH
import glob
import CustomConfiguration
import NewJob
import multiprocessing
import shutil

latestThread = None
histograms =[]
pool= None
analysisComplete = False

def rootAnalysis(**kwargs):
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

    if histograms:
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
        
    
class runThread(threading.Thread):#MARK
    """thread object for running the analysis"""
    
    def __init__(self, params):
        super(runThread,self).__init__()
        self.params = params

    def run(self):        
        rootAnalysis(**self.params)
              
runpressed = False
    
def startRootAnalysis(params):
    """creates an analysis therad"""

    global analysisComplete
    analysisComplete = False
    global latestThread
    latestThread =runThread(params)
    latestThread.setDaemon(True)
    latestThread.start()

def getRootStatus():
    return analysisComplete

if __name__ == '__main__':
    startRootAnalysis()