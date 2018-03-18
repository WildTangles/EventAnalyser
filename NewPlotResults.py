import argparse
import sys
import copy
import os
import glob
import ROOT
import Plotting.PlotStyle as PS
import Plotting.Paintable as Paintable
import Plotting.Depiction as Depiction
import Plotting.Database  as Database
import importlib
import PlotConf_CustomAnalysis
import ImageNames as imn
from collections import OrderedDict
 
def collectPaintables(definition):
    paintables = {}
    for key, item in definition.items():
        if   "Stack" in key: paintables["Stack"] = Paintable.StackPaintable("stack", definition["Stack"])
        elif "data"  in key: paintables["data"]  = Paintable.DataPaintable("data", definition["data"]) 
        else:                paintables[key]     = Paintable.OverlayPaintable(key, definition[key])
    return paintables

def collectDepictions(configuration):
    depictions = []
    definitions = configuration["Definitions"]
    for depiction in configuration["Order"]:
        if definitions[depiction]["type"] == "Main"     : depictions.append(Depiction.MainDepiction(      definitions[depiction], depiction))
        if definitions[depiction]["type"] == "Ratio"    : depictions.append(Depiction.RatioDepiction(     definitions[depiction], depiction))
        if definitions[depiction]["type"] == "Agreement": depictions.append(Depiction.AgreementDepiction( definitions[depiction], depiction))
    return depictions

def initializeDepictions(Depictions):
    n = len(Depictions)
    
    if n == 1:
        Depictions[0].initializeDepiction( 0.0, 0.0, 1.0, 1.0, 0.05, 0.2)        
    elif n == 2:
        Depictions[0].initializeDepiction( 0.0, 0.35, 1.0, 1.0, 0.08,  0.004)
        Depictions[1].initializeDepiction( 0.0, 0.02, 1.0, 0.35, 0.007, 0.05)

    elif n == 3:
        Depictions[0].initializeDepiction( 0.0,  0.5, 1.0,  1.0, 0.1, 0.01)
        Depictions[1].initializeDepiction( 0.0,  0.3, 1.0,  0.5, 0.025, 0.025)
        Depictions[2].initializeDepiction( 0.0,  0.0, 1.0,  0.3, 0.017, 0.5)

    else:
        print "Not Supported Yet"
        sys.exit()
        
    bottomPad = Depictions[-1].pad
    bottomPad.SetBottomMargin(0.1/bottomPad.GetAbsHNDC())

def drawItem(x, y, text, font = 42, size = 0.03, align = 11):
    l = ROOT.TLatex() 
    l.SetNDC();
    l.SetTextAlign(align)                   
    l.SetTextFont(font);
    l.SetTextSize(size)
    l.DrawLatex(x,y,text);

def writeXaxisTitle(Paintables):
    xAxisTitle = Database.histoptions.get("xtitle", Paintables[Paintables.keys()[0]].getHistogram().GetXaxis().GetTitle())
    [p.getHistogram().SetXTitle("") for p in Paintables.values()]
    drawItem(0.95, 0.0675, xAxisTitle, 42, 0.045, 33)
    
def ATLASLabel( x, y):
    drawItem(x    , y,      "ATLAS",              72,  0.03)
    drawItem(x+0.1, y,      "Open Data",          42,  0.03)

def drawLegend(paintables, paintingOrder):
    y1 = 0.92
    y2 = y1 - 0.03*sum([i.getNumberOfLegendItems() for i in paintables.values()])
    legend = ROOT.TLegend(0.70,y1,0.90,y2)  
    legend.SetBorderSize(0)
    for key in paintingOrder:
        paintables[key].addToLegend(legend)
    legend.Draw()
    return legend

def DrawPlot(configuration, histlocation):
    print "Drawing plot: " + histlocation 
    #tImage = ROOT.TImageDump("Output/" + imn.ImageDic[histlocation]+ ".gif")
    canvas = ROOT.TCanvas( histlocation, "title", 900, 900 )
    
    Paintables = collectPaintables(configuration["Paintables"])
    Depictions = collectDepictions(configuration["Depictions"])
    initializeDepictions(Depictions)

    ATLASLabel(0.2,0.90)
    writeXaxisTitle(Paintables)
    # legend has to be attached to canvas otherwise the garbage collector deletes it
    canvas.legend = drawLegend(Paintables, Depictions[0].PaintingOrder)
    [d.drawDepiction(Paintables) for d in Depictions]

    canvas.SaveAs("Output/" + imn.ImageDic[histlocation]+ ".gif")

#======================================================================

def plot_results(samples, histograms):
    """
    Main function to be executed when starting the code.
    """
    ROOT.gROOT.SetBatch()
    ROOT.TGaxis.SetMaxDigits(4)
    ROOT.TH1.AddDirectory(False)
    PS.setStyle();
    
    #parser = argparse.ArgumentParser( description = 'Plotting Tool using YAML files for configuration' )
    #parser.add_argument('configfile', type=str, help='configuration file to be used')
    #configModuleName = "PlotConf_CustomAnalysis"
    #args = parser.parse_args()
    
    #configModuleName = args.configfile.replace("/", ".").strip(".py")

## WARNING:
## IF samples contains nonsense that does not match anything, it returns a garbage skeleton dict.  
    if not samples:
        #default samples
        samples = ['ttbar_lep', 'ttbar_had', 'data_Egamma', 'data_Muons', 'WW', 'WZ', 'ZZ', 'stop_tchan_top', 'stop_tchan_antitop', 'stop_schan', 'stop_wtchan', 'Zee', 'Zmumu', 'Ztautau', 'DYeeM08to15', 'DYeeM15to40', 'DYmumuM08to15', 'DYmumuM15to40', 'DYtautauM08to15', 'DYtautauM15to40', 'WenuWithB', 'WenuJetsBVeto', 'WenuNoJetsBVeto', 'WmunuWithB', 'WmunuJetsBVeto', 'WmunuNoJetsBVeto', 'WtaunuWithB', 'WtaunuJetsBVeto', 'WtaunuNoJetsBVeto']

    configuration = copy.deepcopy(PlotConf_CustomAnalysis.config)

    keptStack = False
    keptData = False

    Z = ["ZPrime400", "ZPrime500", "ZPrime750", "ZPrime1000", "ZPrime1250", "ZPrime1500", "ZPrime1750", "ZPrime2000", "ZPrime2250", "ZPrime2500", "ZPrime3000"]
    keptZ = [False]*len(Z) 

    keptKeys = []        
    tmp = copy.deepcopy(configuration["Paintables"]["Stack"]["Processes"])
    for k, v in tmp.iteritems():
        keepKey = False            
        for j in v["Contributions"]:
            if j in samples:
                keepKey = True
                keptStack = True
                if k not in keptKeys:
                    keptKeys.append(k)                
        if not keepKey:
            del configuration["Paintables"]["Stack"]["Processes"][k]        
    configuration["Paintables"]["Stack"]["Order"] = keptKeys    
    
    cleanContrib = []
    tmp = copy.deepcopy(configuration["Paintables"]["Stack"]["Processes"])
    for k, v in tmp.iteritems():
        for j in v["Contributions"]:
            if j not in samples:
                cleanContrib.append((k, j))
    for i in cleanContrib:            
        configuration["Paintables"]["Stack"]["Processes"][i[0]]["Contributions"].remove(i[1])

    if not configuration["Paintables"]["Stack"]["Processes"].keys():
        del configuration["Paintables"]["Stack"]

    toRemove = []
    for i in configuration["Paintables"]["data"]["Contributions"]:                            
        if i in samples:
            keptData = True
        if i not in samples:
            toRemove.append(i)
    for i in toRemove:        
        configuration["Paintables"]["data"]["Contributions"].remove(i)

    if not configuration["Paintables"]["data"]["Contributions"]:
        del configuration["Paintables"]["data"]


    for idx, Z_i in enumerate(Z,0):
        toRemove = []
        for i in configuration["Paintables"][Z_i]["Contributions"]:
            if i in samples:
                keptZ[idx] = True
            if i not in samples:
                toRemove.append(i)
        for i in toRemove:
            configuration["Paintables"][Z_i]["Contributions"].remove(i)

        if not configuration["Paintables"][Z_i]["Contributions"]:
            del configuration["Paintables"][Z_i]

    if (not keptStack) or (not keptData):                    
        configuration["Depictions"]["Order"].remove("Data/MC")
        del configuration["Depictions"]["Definitions"]["Data/MC"]

    configuration["Depictions"]["Definitions"]["Main"]["Paintables"] = []
    if keptStack:
        configuration["Depictions"]["Definitions"]["Main"]["Paintables"].append("Stack")
    if keptData:
        configuration["Depictions"]["Definitions"]["Main"]["Paintables"].append("data")       
    for idx, keptZ_i in enumerate(keptZ,0):
        if keptZ_i:
            configuration["Depictions"]["Definitions"]["Main"]["Paintables"].append(Z[idx])
    
    Database.config      = dict()
    Database.histoptions = OrderedDict()
    Database.rootFiles   = dict()

    for histogram in histograms:
        Database.UpdateDataBase(configuration, histogram)
        DrawPlot(configuration, histogram)
	
    # Database.config      = dict()
    # Database.histoptions = OrderedDict()
    # Database.rootFiles   = dict()
    
#======================================================================   
#if __name__ == "__main__":
#    main( sys.argv[1:] )
