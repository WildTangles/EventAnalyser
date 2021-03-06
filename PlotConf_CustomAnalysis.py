config = {
"Luminosity": 1000,
"InputDirectory": "results",

"Histograms" : {
    "WtMass"             : {"xtitle" : "m_{T}^{W} [GeV]"},
    "etmiss"             : {"xtitle" : "E_{T}^{Miss} [GeV]"},
    "lep_n"              : {"xndiv" : 10},
    "lep_pt"             : {},
    "lep_eta"            : {},
    "lep_E"              : {},
    "lep_phi"            : {"y_margin" : 1},
    "lep_charge"         : {"y_margin" : 1, "xndiv" : 4},
    "lep_type"           : {"y_margin" : 0.5, "xtitle" : "|PDG id|^{lep}"},
    "leadlep_pt"           : {},
    "leadlep_eta"          : {"y_margin" : 0.5},
    "leadlep_E"            : {},
    "leadlep_phi"          : {"y_margin" : 1},
    "leadlep_charge"       : {"y_margin" : 1, "xndiv" : 4},
    "leadlep_type"         : {"y_margin" : 0.5, "xtitle" : "|PDG id|^{leadlep}"},
    "traillep_pt"          : {},
    "traillep_eta"         : {"y_margin" : 0.5},
    "traillep_E"           : {},
    "traillep_phi"         : {"y_margin" : 1},
    "traillep_charge"      : {"y_margin" : 1, "xndiv" : 4},
    "traillep_type"        : {"y_margin" : 0.5, "xtitle" : "|PDG id|^{traillep}"},
    "deltaTheta"     : {},
    "invMass"              : {"xtitle" : "m_{ll} [GeV]"},
    "invMass2"              : {"xtitle" : "m_{ll} [GeV]"},
    "WtMass"          : {"xtitle" : "m_{T}^{W} [GeV]"},
    "btag"        : {},


   #following 5 were originally commented out - uncommenting for ZPrime reasons
    "lep_ptconerel30"    : {},
    "lep_etconerel20"    : {},
    "lep_d0"             : {},
    "lep_z0"             : {},
    "pvxp_n"             : {},


    "n_jets"             : {"xndiv" : 10},
    "jet_pt"             : {},
    "jet_m"              : {},
    "jet_jvf"            : {"y_margin" : 0.4},
    "jet_eta"            : {"y_margin" : 0.5},
    "jet_MV1"            : {"y_margin" : 0.3},
    "vxp_z"              : {},

},



"Paintables": {
    "Stack": {
        #Diboson added for ZPrime
        "Order"     : ["WW","WZ","ZZ", "DrellYan", "W", "Z", "stop", "ttbar"], #"higgs"
        "Processes" : {

            "WW" : {
                "Color"         : "#fa7921",
                "Contributions" : ["WW"]},
            "WZ" : {
                "Color"         : "#2177f9",
                "Contributions" : ["WZ"]},
            "ZZ" : {
                "Color"         : "#fc1bb1",
                "Contributions" : ["ZZ"]},
                                
            "DrellYan": {       
                "Color"         : "#5bc0eb",
                "Contributions" : ["DYeeM08to15", "DYeeM15to40", "DYmumuM08to15", "DYmumuM15to40", "DYtautauM08to15", "DYtautauM15to40"]},
            
            "W": {              
                "Color"         : "#e55934",
                "Contributions" : ["WenuJetsBVeto", "WenuWithB", "WenuNoJetsBVeto", "WmunuJetsBVeto", "WmunuWithB", "WmunuNoJetsBVeto", "WtaunuJetsBVeto", "WtaunuWithB", "WtaunuNoJetsBVeto"]},
                                
            "Z": {              
                "Color"         : "#086788",
                "Contributions" : ["Zee", "Zmumu", "Ztautau"]},
                  
            "stop": {
                "Color"         : "#fde74c",
                "Contributions" : ["stop_tchan_top", "stop_tchan_antitop", "stop_schan", "stop_wtchan"]},
            
            "ttbar": {
                "Color"         : "#9bc53d",
                "Contributions" : ["ttbar_lep", "ttbar_had"]},

            # "Higgs": {
            #     "Color": "#0000ff",
            #     "Contributions": ["ggH125_WW2lep", "VBFH125_WW2lep", "VBFH125_ZZ4lep", "ggH125_ZZ4lep"]},
        }
    },

    #following added for ZPrime obviously
    "ZPrime400": {
        "Color": "#ff0000",
        "Scale": 10,
        "Contributions": ["ZPrime400"]},

    "ZPrime500": {
        "Color": "#ff6100",
        "Scale": 10,
        "Contributions": ["ZPrime500"]},

    "ZPrime750": {
        "Color": "#ffc700",
        "Scale": 10,
        "Contributions": ["ZPrime750"]},

    "ZPrime1000": {
        "Color": "#c7ff00",
        "Scale": 10,
        "Contributions": ["ZPrime1000"]},

    "ZPrime1250": {
        "Color": "#4cff00",
        "Scale": 10,
        "Contributions": ["ZPrime1250"]},

    "ZPrime1500": {
        "Color": "#00ff3b",
        "Scale": 10,
        "Contributions": ["ZPrime1500"]},

    "ZPrime1750": {
        "Color": "#00ffa9",
        "Scale": 10,
        "Contributions": ["ZPrime1750"]},

    "ZPrime2000": {
        "Color" : "#00f2ff",
        "Scale" : 10,
        "Contributions" : ["ZPrime2000"]},

    "ZPrime2250": {
        "Color" : "#007bff",
        "Scale" : 10,
        "Contributions" : ["ZPrime2250"]},

    "ZPrime2500": {
        "Color" : "#3700ff",
        "Scale" : 10,
        "Contributions" : ["ZPrime2500"]},

    "ZPrime3000": {
        "Color" : "#b200ff",
        "Scale" : 10,
        "Contributions" : ["ZPrime3000"]},


    "data" : {
        "Contributions": ["data_Egamma", "data_Muons"]}
},

"Depictions": {
    "Order": ["Main", "Data/MC"],
    "Definitions" : {
        "Data/MC": {
            "type"       : "Agreement",
            "Paintables" : ["data", "Stack"]
        },
        
        "Main": {
            "type"      : "Main",
            "Paintables": ["Stack", "data", "ZPrime400", "ZPrime500", "ZPrime750", "ZPrime1000", "ZPrime1250", "ZPrime1500", "ZPrime1750", "ZPrime2000", "ZPrime2250", "ZPrime2500", "ZPrime3000"]
        },

        # 'S/B': {
        #     'type': 'Ratio',
        #     'Paintables': ['Higgs', 'Stack']},
    }
},
}

#pre Z prime changes below.
# config = {
# "Luminosity": 1000,
# "InputDirectory": "results",

# "Histograms" : {
#     "WtMass"             : {"xtitle" : "m_{T}^{W} [GeV]"},
#     "etmiss"             : {"xtitle" : "E_{T}^{Miss} [GeV]"},
#     "lep_n"              : {"xndiv" : 10},
#     "lep_pt"             : {},
#     "lep_eta"            : {},
#     "lep_E"              : {},
#     "lep_phi"            : {"y_margin" : 1},
#     "lep_charge"         : {"y_margin" : 1, "xndiv" : 4},
#     "lep_type"           : {"y_margin" : 0.5, "xtitle" : "|PDG id|^{lep}"},
#     "leadlep_pt"           : {},
#     "leadlep_eta"          : {"y_margin" : 0.5},
#     "leadlep_E"            : {},
#     "leadlep_phi"          : {"y_margin" : 1},
#     "leadlep_charge"       : {"y_margin" : 1, "xndiv" : 4},
#     "leadlep_type"         : {"y_margin" : 0.5, "xtitle" : "|PDG id|^{leadlep}"},
#     "traillep_pt"          : {},
#     "traillep_eta"         : {"y_margin" : 0.5},
#     "traillep_E"           : {},
#     "traillep_phi"         : {"y_margin" : 1},
#     "traillep_charge"      : {"y_margin" : 1, "xndiv" : 4},
#     "traillep_type"        : {"y_margin" : 0.5, "xtitle" : "|PDG id|^{traillep}"},
#     "deltaTheta"     : {},
#     "invMass"              : {"xtitle" : "m_{ll} [GeV]"},
#     "invMass2"              : {"xtitle" : "m_{ll} [GeV]"},
#     "WtMass"          : {"xtitle" : "m_{T}^{W} [GeV]"},
#     "btag"        : {},


   
#    # "lep_ptconerel30"    : {},
#    # "lep_etconerel20"    : {},
#    # "lep_d0"             : {},
#    # "lep_z0"             : {},
#     "n_jets"             : {"xndiv" : 10},
#     "jet_pt"             : {},
#     "jet_m"              : {},
#     "jet_jvf"            : {"y_margin" : 0.4},
#     "jet_eta"            : {"y_margin" : 0.5},
#     "jet_MV1"            : {"y_margin" : 0.3},
#     "vxp_z"              : {},
#    # "pvxp_n"             : {},
# },

# "Paintables": {
#     "Stack": {
#         "Order"     : ["WW","WZ","ZZ", "DrellYan", "W", "Z", "stop", "ttbar"],
#         "Processes" : {                
#             "WW" : {
#                 "Color"         : "#fa7921",
#                 "Contributions" : ["WW"]},
#             "WZ" : {
#                 "Color"         : "#2177f9",
#                 "Contributions" : ["WZ"]},
#             "ZZ" : {
#                 "Color"         : "#fc1bb1",
#                 "Contributions" : ["ZZ"]},
                                
#             "DrellYan": {       
#                 "Color"         : "#5bc0eb",
#                 "Contributions" : ["DYeeM08to15", "DYeeM15to40", "DYmumuM08to15", "DYmumuM15to40", "DYtautauM08to15", "DYtautauM15to40"]},
            
#             "W": {              
#                 "Color"         : "#e55934",
#                 "Contributions" : ["WenuJetsBVeto", "WenuWithB", "WenuNoJetsBVeto", "WmunuJetsBVeto", "WmunuWithB", "WmunuNoJetsBVeto", "WtaunuJetsBVeto", "WtaunuWithB", "WtaunuNoJetsBVeto"]},
                                
#             "Z": {              
#                 "Color"         : "#086788",
#                 "Contributions" : ["Zee", "Zmumu", "Ztautau"]},
                  
#             "stop": {
#                 "Color"         : "#fde74c",
#                 "Contributions" : ["stop_tchan_top", "stop_tchan_antitop", "stop_schan", "stop_wtchan"]},
            
#             "ttbar": {
#                 "Color"         : "#9bc53d",
#                 "Contributions" : ["ttbar_lep", "ttbar_had"]}
#         }
#     },

#     "data" : {
#         "Contributions": ["data_Egamma", "data_Muons"]}
# },

# "Depictions": {
#     "Order": ["Main", "Data/MC"],
#     "Definitions" : {
#         "Data/MC": {
#             "type"       : "Agreement",
#             "Paintables" : ["data", "Stack"]
#         },
        
#         "Main": {
#             "type"      : "Main",
#             "Paintables": ["Stack", "data"]
#         },
#     }
# },
# }