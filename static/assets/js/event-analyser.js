// checkbox prompt toggles
MTMprompt = $('#missing-transverse-momentum-prompts'),
MTMcheckbox = $('#missing-transverse-momentum-checkbox');

JETprompt = $('#number-jets-prompts'),
JETcheckbox = $('#number-jets-checkbox'),
bJETprompt = $('#number-b-jets-prompts'),
bJETcheckbox = $('#number-b-jets-checkbox'),
bJETcheckboxgroup = $('#number-b-jets-checkbox-group'),
bJETcheckboxhelp = $('#number-b-jets-checkbox-help');

LEPNUMcheckbox = $('#number-charged-leptons'),
LEPNUMprompt = $('#number-charged-leptons-prompts-number');

LEPTMprompt = $('#number-charged-leptons-prompts-transverse-mass');

LEPchargeprompt = $('#number-charged-leptons-prompts-charge'),
chargeSamecheckbox = $('#number-charged-leptons-prompts-charge-same'),
chargeOppcheckbox = $('#number-charged-leptons-prompts-charge-opp');

LEPflavorprompt = $('#number-charged-leptons-prompts-flavor'),
flavorSamecheckbox = $('#number-charged-leptons-prompts-flavor-same'),
flavorDiffcheckbox = $('#number-charged-leptons-prompts-flavor-diff');

LEP1IMprompt = $('#number-charged-leptons-prompts-invariant-mass1');

LEP2IMprompt = $('#number-charged-leptons-prompts-invariant-mass2');

minLEPMcheckboxgroup = $('#min-charged-lepton-transverse-momentum-checkbox-group'),
minLEPMcheckbox = $('#min-charged-lepton-transverse-momentum-checkbox'),
minLEPMprompt = $('#number-charged-leptons-prompts-min-transverse-momentum-inner');

DSC = $('#data-samples-checkbox');

EXP = $('#data-samples-checkbox-experimental-grp');
EXPCB = $('#data-samples-checkbox-experimental');
EXPALL = $('#data-samples-checkbox-experimental-options');
EXPEG = $('#data-samples-checkbox-experimental-options-EGamma');
EXPM = $('#data-samples-checkbox-experimental-options-Muons');

SIM = $('#data-samples-checkbox-simulated-grp');
SIMCB = $('#data-samples-checkbox-simulated');
SIMSM = $('#data-samples-checkbox-simulated-SM-grp');
SIMSMCB = $('#data-samples-checkbox-simulated-SM');
SIMSMCB = $('#data-samples-checkbox-simulated-SM');

SIMDB = $('#data-samples-checkbox-simulated-SM-Diboson-grp');
SIMDBCB = $('#data-samples-checkbox-simulated-SM-Diboson');
SIMDBALL = $('#data-samples-checkbox-simulated-SM-Diboson-options');
SIMDBWW = $('#data-samples-checkbox-simulated-SM-Diboson-WW');
SIMDBZZ = $('#data-samples-checkbox-simulated-SM-Diboson-ZZ');
SIMDBWZ = $('#data-samples-checkbox-simulated-SM-Diboson-WZ');

SIMSTQP = $('#data-samples-checkbox-simulated-SM-STQP-grp');
SIMSTQPCB = $('#data-samples-checkbox-simulated-SM-STQP');
SIMSTQPALL1 = $('#data-samples-checkbox-simulated-SM-STQP1');
SIMSTQPALL2 = $('#data-samples-checkbox-simulated-SM-STQP2');
SIMSTQPTT = $('#data-samples-checkbox-simulated-SM-STQP-TT');
SIMSTQPTAT = $('#data-samples-checkbox-simulated-SM-STQP-TAT');
SIMSTQPS = $('#data-samples-checkbox-simulated-SM-STQP-S');
SIMSTQPWT = $('#data-samples-checkbox-simulated-SM-STQP-WT');

SIMSMZP = $('#data-samples-checkbox-simulated-SM-ZP-grp');
SIMSMZPCB = $('#data-samples-checkbox-simulated-SM-ZP');
SIMSMZPALL = $('#data-samples-checkbox-simulated-SM-ZP1');
SIMSMZPEE = $('#data-samples-checkbox-simulated-SM-ZP-ZEE');
SIMSMZPMM = $('#data-samples-checkbox-simulated-SM-ZP-ZMM');
SIMSMZPTT = $('#data-samples-checkbox-simulated-SM-ZP-ZTT');

SIMDY = $('#data-samples-checkbox-simulated-SM-DY-grp');
SIMDYCB = $('#data-samples-checkbox-simulated-SM-DY');
SIMDY1 = $('#data-samples-checkbox-simulated-SM-DY1');
SIMDY2 = $('#data-samples-checkbox-simulated-SM-DY2');
SIMDYEE1 = $('#data-samples-checkbox-simulated-SM-DY-EE0815');
SIMDYEE2 = $('#data-samples-checkbox-simulated-SM-DY-EE1540');
SIMDYTT1 = $('#data-samples-checkbox-simulated-SM-DY-TT0815');
SIMDYTT2 = $('#data-samples-checkbox-simulated-SM-DY-TT1540');
SIMDYMM1 = $('#data-samples-checkbox-simulated-SM-DY-MM0815');
SIMDYMM2 = $('#data-samples-checkbox-simulated-SM-DY-MM1540');

SIMWP = $('#data-samples-checkbox-simulated-SM-WP-grp');
SIMWPCB = $('#data-samples-checkbox-simulated-SM-WP');
SIMWP1 = $('#data-samples-checkbox-simulated-SM-WP1');
SIMWP2 = $('#data-samples-checkbox-simulated-SM-WP2');
SIMWP3 = $('#data-samples-checkbox-simulated-SM-WP3');
SIMWPEVB = $('#data-samples-checkbox-simulated-SM-WP-EVB');
SIMWPEVBV = $('#data-samples-checkbox-simulated-SM-WP-EVBV');
SIMWPEVNBV = $('#data-samples-checkbox-simulated-SM-WP-EVNBV');
SIMWPTVB = $('#data-samples-checkbox-simulated-SM-WP-TVB');
SIMWPTVBV = $('#data-samples-checkbox-simulated-SM-WP-TVBV');
SIMWPTVNBV = $('#data-samples-checkbox-simulated-SM-WP-TVNBV');
SIMWPWVB = $('#data-samples-checkbox-simulated-SM-WP-WVB');
SIMWPWVBV = $('#data-samples-checkbox-simulated-SM-WP-WVBV');
SIMWPWVNBV = $('#data-samples-checkbox-simulated-SM-WP-WVNBV');

SIMBSM = $('#data-samples-checkbox-simulated-BSM-grp');
SIMBSMCB = $('#data-samples-checkbox-simulated-BSM');
SIMZP = $('#data-samples-checkbox-simulated-BSM-ZP-grp');
SIMZPCB = $('#data-samples-checkbox-simulated-BSM-ZP');
SIMZP1 = $('#data-samples-checkbox-simulated-BSM-ZP1');
SIMZP2 = $('#data-samples-checkbox-simulated-BSM-ZP2');
SIMZP3 = $('#data-samples-checkbox-simulated-BSM-ZP3');
SIMZP4 = $('#data-samples-checkbox-simulated-BSM-ZP4');
SIMZP400 = $('#data-samples-checkbox-simulated-BSM-ZP-400');
SIMZP500 = $('#data-samples-checkbox-simulated-BSM-ZP-500');
SIMZP750 = $('#data-samples-checkbox-simulated-BSM-ZP-750');
SIMZP1000 = $('#data-samples-checkbox-simulated-BSM-ZP-1000');
SIMZP1250 = $('#data-samples-checkbox-simulated-BSM-ZP-1250');
SIMZP1500 = $('#data-samples-checkbox-simulated-BSM-ZP-1500');
SIMZP1750 = $('#data-samples-checkbox-simulated-BSM-ZP-1750');
SIMZP2000 = $('#data-samples-checkbox-simulated-BSM-ZP-2000');
SIMZP2250 = $('#data-samples-checkbox-simulated-BSM-ZP-2250');
SIMZP2500 = $('#data-samples-checkbox-simulated-BSM-ZP-2500');
SIMZP3000 = $('#data-samples-checkbox-simulated-BSM-ZP-3000');


EXPALL.hide();
EXP.hide();

SIM.hide();
SIMSM.hide();
SIMDB.hide();
SIMDBALL.hide();

SIMSTQP.hide();
SIMSTQPALL1.hide();
SIMSTQPALL2.hide();

SIMSMZP.hide();
SIMSMZPALL.hide();

SIMDY.hide();
SIMDY1.hide();
SIMDY2.hide();

SIMWP.hide();
SIMWP1.hide();
SIMWP2.hide();
SIMWP3.hide();

SIMBSM.hide();
SIMZP.hide();
SIMZP1.hide();
SIMZP2.hide();
SIMZP3.hide();
SIMZP4.hide();

headerText = $('#lead-text');

GO = $('#GO');

MTMprompt.hide();
JETprompt.hide();
bJETcheckboxgroup.hide();
bJETcheckboxhelp.hide();
bJETprompt.hide();

LEPTMprompt.hide();
LEPchargeprompt.hide();
LEPflavorprompt.hide();
LEP1IMprompt.hide();
LEP2IMprompt.hide();
LEPNUMprompt.hide();

minLEPMcheckboxgroup.hide();
minLEPMprompt.hide();

minLEPMcheckbox.on('click', function(){
    if($(this).is(':checked')){
        minLEPMprompt.show();
        minLEPMprompt.find('input').val(' ');
        minLEPMprompt.find('input').attr('required', true);
    } else {
        minLEPMprompt.hide();
        minLEPMprompt.find('input').val(' ');
        minLEPMprompt.find('input').attr('required', false);
    }
});

LEPNUMcheckbox.on('click', function(){
  if($(this).is(':checked')){
    LEPNUMprompt.show();
  } else {
    LEPNUMprompt.hide();
    LEPTMprompt.hide();
    LEPTMprompt.find('input').val(' ');    
    LEPTMprompt.find('input').attr('required', false);
    LEP1IMprompt.hide();
    LEP1IMprompt.find('input').val(' ');
    LEP1IMprompt.find('input').attr('required', false);
    LEP2IMprompt.hide();
    LEP2IMprompt.find('input').val(' ');
    LEP2IMprompt.find('input').attr('required', false);
    LEPchargeprompt.hide();
    LEPflavorprompt.hide();
    chargeOppcheckbox.prop('checked', false);
    chargeSamecheckbox.prop('checked', false);
    flavorDiffcheckbox.prop('checked', false);
    flavorSamecheckbox.prop('checked', false);    

    minLEPMcheckboxgroup.hide();
    minLEPMcheckbox.prop('checked', false);
    minLEPMprompt.hide();
    minLEPMprompt.find('input').val(' ');
    minLEPMprompt.find('input').attr('required', false);
  }
});

$('.btn-group-toggle input[type=radio]').on('change', function() {
  if($('#number-charged-leptons-0').is(':checked')){    
    LEPTMprompt.hide();
    LEPTMprompt.find('input').val(' ');
    LEPTMprompt.find('input').attr('required', false);
    LEPchargeprompt.hide();
    LEPflavorprompt.hide();
    chargeOppcheckbox.prop('checked', false);
    chargeSamecheckbox.prop('checked', false);
    flavorDiffcheckbox.prop('checked', false);
    flavorSamecheckbox.prop('checked', false);    
    LEP1IMprompt.hide();
    LEP1IMprompt.find('input').val(' ');
    LEP1IMprompt.find('input').attr('required', false);
    LEP2IMprompt.hide();
    LEP2IMprompt.find('input').val(' ');
    LEP2IMprompt.find('input').attr('required', false);

    minLEPMcheckboxgroup.hide();
    minLEPMcheckbox.prop('checked', false);
    minLEPMprompt.hide();
    minLEPMprompt.find('input').val(' ');
    minLEPMprompt.find('input').attr('required', false);
  } else if($('#number-charged-leptons-1').is(':checked')){        
    LEPTMprompt.show();
    LEPTMprompt.find('input').attr('required', true);

    //LEPTMprompt.hide();    
    LEPTMprompt.find('input').val(' ');
    LEPchargeprompt.hide();
    LEPflavorprompt.hide();
    chargeOppcheckbox.prop('checked', false);
    chargeSamecheckbox.prop('checked', false);
    flavorDiffcheckbox.prop('checked', false);
    flavorSamecheckbox.prop('checked', false);    
    LEP1IMprompt.hide();
    LEP1IMprompt.find('input').val(' ');
    LEP1IMprompt.find('input').attr('required', false);
    LEP2IMprompt.hide();
    LEP2IMprompt.find('input').val(' ');   
    LEP2IMprompt.find('input').attr('required', false);   

    minLEPMcheckboxgroup.show();
    minLEPMcheckbox.prop('checked', false);
    minLEPMprompt.hide();
    minLEPMprompt.find('input').val(' ');
    minLEPMprompt.find('input').attr('required', false);
  } else if($('#number-charged-leptons-2').is(':checked')){
    LEPchargeprompt.show();
    LEPflavorprompt.show();
    LEP1IMprompt.show();
    LEP1IMprompt.find('input').attr('required', true);

    LEPTMprompt.hide();
    LEPTMprompt.find('input').val(' ');
    LEPTMprompt.find('input').attr('required', false);
    //LEPchargeprompt.hide();
    //LEPflavorprompt.hide();
    chargeOppcheckbox.prop('checked', false);
    chargeSamecheckbox.prop('checked', false);
    flavorDiffcheckbox.prop('checked', false);
    flavorSamecheckbox.prop('checked', false);    
    //LEP1IMprompt.hide();
    LEP1IMprompt.find('input').val(' ');
    LEP2IMprompt.hide();
    LEP2IMprompt.find('input').val(' ');
    LEP2IMprompt.find('input').attr('required', false);

    minLEPMcheckboxgroup.show();
    minLEPMcheckbox.prop('checked', false);
    minLEPMprompt.hide();
    minLEPMprompt.find('input').val(' ');
    minLEPMprompt.find('input').attr('required', false);
  } else if($('#number-charged-leptons-3').is(':checked')){
    LEPTMprompt.show();
    LEPTMprompt.find('input').attr('required', true);
    LEPchargeprompt.show();
    LEPflavorprompt.show();
    LEP1IMprompt.show();
    LEP1IMprompt.find('input').attr('required', true);

    //LEPTMprompt.hide();
    LEPTMprompt.find('input').val(' ');
    //LEPchargeprompt.hide();
    //LEPflavorprompt.hide();
    chargeOppcheckbox.prop('checked', false);
    chargeSamecheckbox.prop('checked', false);
    flavorDiffcheckbox.prop('checked', false);
    flavorSamecheckbox.prop('checked', false);    
    //LEP1IMprompt.hide();
    LEP1IMprompt.find('input').val(' ');
    LEP2IMprompt.hide();
    LEP2IMprompt.find('input').val(' ');
    LEP2IMprompt.find('input').attr('required', false);

    minLEPMcheckboxgroup.show();
    minLEPMcheckbox.prop('checked', false);
    minLEPMprompt.hide();
    minLEPMprompt.find('input').val(' ');
    minLEPMprompt.find('input').attr('required', false);
  } else if($('#number-charged-leptons-4').is(':checked')){    
    LEPchargeprompt.show();
    LEPflavorprompt.show();
    LEP1IMprompt.show();
    LEP1IMprompt.find('input').attr('required', true);
    LEP2IMprompt.show();
    LEP2IMprompt.find('input').attr('required', true);


    LEPTMprompt.hide();
    LEPTMprompt.find('input').val(' ');
    LEPTMprompt.find('input').attr('required', false);
    //LEPchargeprompt.hide();
    //LEPflavorprompt.hide();
    chargeOppcheckbox.prop('checked', false);
    chargeSamecheckbox.prop('checked', false);
    flavorDiffcheckbox.prop('checked', false);
    flavorSamecheckbox.prop('checked', false);    
    //LEP1IMprompt.hide();
    LEP1IMprompt.find('input').val(' ');
    //LEP2IMprompt.hide();
    LEP2IMprompt.find('input').val(' ');

    minLEPMcheckboxgroup.show();
    minLEPMcheckbox.prop('checked', false);
    minLEPMprompt.hide();
    minLEPMprompt.find('input').val(' ');
    minLEPMprompt.find('input').attr('required', false);
  }
});

chargeSamecheckbox.on('click', function(){
  if($(this).is(':checked')){
    chargeOppcheckbox.prop('checked', false);          
  }
});

chargeOppcheckbox.on('click', function(){
  if($(this).is(':checked')){
    chargeSamecheckbox.prop('checked', false);          
  }
});

flavorSamecheckbox.on('click', function(){
  if($(this).is(':checked')){
    flavorDiffcheckbox.prop('checked', false);
  }
});

flavorDiffcheckbox.on('click', function(){
  if($(this).is(':checked')){
    flavorSamecheckbox.prop('checked', false);
  }
});

MTMcheckbox.on('click', function(){
  if($(this).is(':checked')){
    MTMprompt.show();
    MTMprompt.find('input').attr('required', true);
    MTMprompt.find('input').val(' ');
  } else {
    MTMprompt.hide();
    MTMprompt.find('input').attr('required', false);
    MTMprompt.find('input').val(' ');
  }
});



JETcheckbox.on('click', function(){
  if($(this).is(':checked')){
    JETprompt.show();
    bJETcheckboxgroup.show();
    bJETcheckboxhelp.show();
    JETprompt.find('input').attr('required', true);
    JETprompt.find('input').val(' ');
    bJETprompt.find('input').val(' ');
  } else {
    JETprompt.hide();
    bJETprompt.hide();
    bJETcheckboxgroup.hide();
    bJETcheckboxhelp.hide();
    JETprompt.find('input').attr('required', false);
    JETprompt.find('input').val(' ');
    bJETprompt.find('input').attr('required', false);
    bJETprompt.find('input').val(' ');
    bJETcheckbox.prop('checked', false);
  }
});

bJETcheckbox.on('click', function(){
  if($(this).is(':checked')){
    bJETprompt.show();
    bJETprompt.find('input').attr('required', true);
    bJETprompt.find('input').val(' ');
  } else {
    bJETprompt.hide();
    bJETprompt.find('input').attr('required', false);
    bJETprompt.find('input').val(' ');
  }
});

DSC.on('click', function(){
  if($(this).is(':checked')){

EXPALL.hide();
EXP.show();

SIM.show();
SIMSM.hide();
SIMDB.hide();
SIMDBALL.hide();

SIMSTQP.hide();
SIMSTQPALL1.hide();
SIMSTQPALL2.hide();

SIMSMZP.hide();
SIMSMZPALL.hide();

SIMDY.hide();
SIMDY1.hide();
SIMDY2.hide();

SIMWP.hide();
SIMWP1.hide();
SIMWP2.hide();
SIMWP3.hide();

SIMBSM.hide();
SIMZP.hide();
SIMZP1.hide();
SIMZP2.hide();
SIMZP3.hide();
SIMZP4.hide();

EXPCB.prop('checked', false);
EXPEG.prop('checked', false);
EXPM.prop('checked', false);

SIMCB.prop('checked', false);

SIMSMCB.prop('checked', false);

SIMDBCB.prop('checked', false);
SIMDBWW.prop('checked', false);
SIMDBZZ.prop('checked', false);
SIMDBWZ.prop('checked', false);

SIMSTQPCB.prop('checked', false);
SIMSTQPTT.prop('checked', false);
SIMSTQPTAT.prop('checked', false);
SIMSTQPS.prop('checked', false);
SIMSTQPWT.prop('checked', false);

SIMSMZPCB.prop('checked', false);
SIMSMZPEE.prop('checked', false);
SIMSMZPMM.prop('checked', false);
SIMSMZPTT.prop('checked', false);

SIMDYCB.prop('checked', false);
SIMDYEE1.prop('checked', false);
SIMDYEE2.prop('checked', false);
SIMDYTT1.prop('checked', false);
SIMDYTT2.prop('checked', false);
SIMDYMM1.prop('checked', false);
SIMDYMM2.prop('checked', false);

SIMWPCB.prop('checked', false);
SIMWPEVB.prop('checked', false);
SIMWPEVBV.prop('checked', false);
SIMWPEVNBV.prop('checked', false);
SIMWPTVB.prop('checked', false);
SIMWPTVBV.prop('checked', false);
SIMWPTVNBV.prop('checked', false);
SIMWPWVB.prop('checked', false);
SIMWPWVBV.prop('checked', false);
SIMWPWVNBV.prop('checked', false);

SIMBSMCB.prop('checked', false);

SIMZPCB.prop('checked', false);
SIMZP400.prop('checked', false);
SIMZP500.prop('checked', false);
SIMZP750.prop('checked', false);
SIMZP1000.prop('checked', false);
SIMZP1250.prop('checked', false);
SIMZP1500.prop('checked', false);
SIMZP1750.prop('checked', false);
SIMZP2000.prop('checked', false);
SIMZP2250.prop('checked', false);
SIMZP2500.prop('checked', false);
SIMZP3000.prop('checked', false);

  } else {

EXPALL.hide();
EXP.hide();

SIM.hide();
SIMSM.hide();
SIMDB.hide();
SIMDBALL.hide();

SIMSTQP.hide();
SIMSTQPALL1.hide();
SIMSTQPALL2.hide();

SIMSMZP.hide();
SIMSMZPALL.hide();

SIMDY.hide();
SIMDY1.hide();
SIMDY2.hide();

SIMWP.hide();
SIMWP1.hide();
SIMWP2.hide();
SIMWP3.hide();

SIMBSM.hide();
SIMZP.hide();
SIMZP1.hide();
SIMZP2.hide();
SIMZP3.hide();
SIMZP4.hide();

EXPCB.prop('checked', false);
EXPEG.prop('checked', false);
EXPM.prop('checked', false);

SIMCB.prop('checked', false);

SIMSMCB.prop('checked', false);

SIMDBCB.prop('checked', false);
SIMDBWW.prop('checked', false);
SIMDBZZ.prop('checked', false);
SIMDBWZ.prop('checked', false);

SIMSTQPCB.prop('checked', false);
SIMSTQPTT.prop('checked', false);
SIMSTQPTAT.prop('checked', false);
SIMSTQPS.prop('checked', false);
SIMSTQPWT.prop('checked', false);

SIMSMZPCB.prop('checked', false);
SIMSMZPEE.prop('checked', false);
SIMSMZPMM.prop('checked', false);
SIMSMZPTT.prop('checked', false);

SIMDYCB.prop('checked', false);
SIMDYEE1.prop('checked', false);
SIMDYEE2.prop('checked', false);
SIMDYTT1.prop('checked', false);
SIMDYTT2.prop('checked', false);
SIMDYMM1.prop('checked', false);
SIMDYMM2.prop('checked', false);

SIMWPCB.prop('checked', false);
SIMWPEVB.prop('checked', false);
SIMWPEVBV.prop('checked', false);
SIMWPEVNBV.prop('checked', false);
SIMWPTVB.prop('checked', false);
SIMWPTVBV.prop('checked', false);
SIMWPTVNBV.prop('checked', false);
SIMWPWVB.prop('checked', false);
SIMWPWVBV.prop('checked', false);
SIMWPWVNBV.prop('checked', false);

SIMBSMCB.prop('checked', false);

SIMZPCB.prop('checked', false);
SIMZP400.prop('checked', false);
SIMZP500.prop('checked', false);
SIMZP750.prop('checked', false);
SIMZP1000.prop('checked', false);
SIMZP1250.prop('checked', false);
SIMZP1500.prop('checked', false);
SIMZP1750.prop('checked', false);
SIMZP2000.prop('checked', false);
SIMZP2250.prop('checked', false);
SIMZP2500.prop('checked', false);
SIMZP3000.prop('checked', false);

  }
});

JETcheckbox.on('click', function(){
  if($(this).is(':checked')){
    JETprompt.show();
    bJETcheckboxgroup.show();
    bJETcheckboxhelp.show();
    JETprompt.find('input').attr('required', true);
    JETprompt.find('input').val(' ');
    bJETprompt.find('input').val(' ');
  } else {
    JETprompt.hide();
    bJETprompt.hide();
    bJETcheckboxgroup.hide();
    bJETcheckboxhelp.hide();
    JETprompt.find('input').attr('required', false);
    JETprompt.find('input').val(' ');
    bJETprompt.find('input').attr('required', false);
    bJETprompt.find('input').val(' ');
    bJETcheckbox.prop('checked', false);
  }
});

EXPCB.on('click', function(){
    if($(this).is(':checked')){
        EXPALL.show();
        EXPEG.prop('checked', false);
        EXPM.prop('checked', false);
    } else {
        EXPALL.hide();
        EXPEG.prop('checked', false);
        EXPM.prop('checked', false);
    }
});

SIMCB.on('click', function(){
    if($(this).is(':checked')){

SIMSM.show();
SIMDB.hide();
SIMDBALL.hide();

SIMSTQP.hide();
SIMSTQPALL1.hide();
SIMSTQPALL2.hide();

SIMSMZP.hide();
SIMSMZPALL.hide();

SIMDY.hide();
SIMDY1.hide();
SIMDY2.hide();

SIMWP.hide();
SIMWP1.hide();
SIMWP2.hide();
SIMWP3.hide();

SIMBSM.show();
SIMZP.hide();
SIMZP1.hide();
SIMZP2.hide();
SIMZP3.hide();
SIMZP4.hide();

SIMSMCB.prop('checked', false);

SIMDBCB.prop('checked', false);
SIMDBWW.prop('checked', false);
SIMDBZZ.prop('checked', false);
SIMDBWZ.prop('checked', false);

SIMSTQPCB.prop('checked', false);
SIMSTQPTT.prop('checked', false);
SIMSTQPTAT.prop('checked', false);
SIMSTQPS.prop('checked', false);
SIMSTQPWT.prop('checked', false);

SIMSMZPCB.prop('checked', false);
SIMSMZPEE.prop('checked', false);
SIMSMZPMM.prop('checked', false);
SIMSMZPTT.prop('checked', false);

SIMDYCB.prop('checked', false);
SIMDYEE1.prop('checked', false);
SIMDYEE2.prop('checked', false);
SIMDYTT1.prop('checked', false);
SIMDYTT2.prop('checked', false);
SIMDYMM1.prop('checked', false);
SIMDYMM2.prop('checked', false);

SIMWPCB.prop('checked', false);
SIMWPEVB.prop('checked', false);
SIMWPEVBV.prop('checked', false);
SIMWPEVNBV.prop('checked', false);
SIMWPTVB.prop('checked', false);
SIMWPTVBV.prop('checked', false);
SIMWPTVNBV.prop('checked', false);
SIMWPWVB.prop('checked', false);
SIMWPWVBV.prop('checked', false);
SIMWPWVNBV.prop('checked', false);

SIMBSMCB.prop('checked', false);

SIMZPCB.prop('checked', false);
SIMZP400.prop('checked', false);
SIMZP500.prop('checked', false);
SIMZP750.prop('checked', false);
SIMZP1000.prop('checked', false);
SIMZP1250.prop('checked', false);
SIMZP1500.prop('checked', false);
SIMZP1750.prop('checked', false);
SIMZP2000.prop('checked', false);
SIMZP2250.prop('checked', false);
SIMZP2500.prop('checked', false);
SIMZP3000.prop('checked', false);

    } else {

SIMSM.hide();
SIMDB.hide();
SIMDBALL.hide();

SIMSTQP.hide();
SIMSTQPALL1.hide();
SIMSTQPALL2.hide();

SIMSMZP.hide();
SIMSMZPALL.hide();

SIMDY.hide();
SIMDY1.hide();
SIMDY2.hide();

SIMWP.hide();
SIMWP1.hide();
SIMWP2.hide();
SIMWP3.hide();

SIMBSM.hide();
SIMZP.hide();
SIMZP1.hide();
SIMZP2.hide();
SIMZP3.hide();
SIMZP4.hide();

SIMSMCB.prop('checked', false);

SIMDBCB.prop('checked', false);
SIMDBWW.prop('checked', false);
SIMDBZZ.prop('checked', false);
SIMDBWZ.prop('checked', false);

SIMSTQPCB.prop('checked', false);
SIMSTQPTT.prop('checked', false);
SIMSTQPTAT.prop('checked', false);
SIMSTQPS.prop('checked', false);
SIMSTQPWT.prop('checked', false);

SIMSMZPCB.prop('checked', false);
SIMSMZPEE.prop('checked', false);
SIMSMZPMM.prop('checked', false);
SIMSMZPTT.prop('checked', false);

SIMDYCB.prop('checked', false);
SIMDYEE1.prop('checked', false);
SIMDYEE2.prop('checked', false);
SIMDYTT1.prop('checked', false);
SIMDYTT2.prop('checked', false);
SIMDYMM1.prop('checked', false);
SIMDYMM2.prop('checked', false);

SIMWPCB.prop('checked', false);
SIMWPEVB.prop('checked', false);
SIMWPEVBV.prop('checked', false);
SIMWPEVNBV.prop('checked', false);
SIMWPTVB.prop('checked', false);
SIMWPTVBV.prop('checked', false);
SIMWPTVNBV.prop('checked', false);
SIMWPWVB.prop('checked', false);
SIMWPWVBV.prop('checked', false);
SIMWPWVNBV.prop('checked', false);

SIMBSMCB.prop('checked', false);

SIMZPCB.prop('checked', false);
SIMZP400.prop('checked', false);
SIMZP500.prop('checked', false);
SIMZP750.prop('checked', false);
SIMZP1000.prop('checked', false);
SIMZP1250.prop('checked', false);
SIMZP1500.prop('checked', false);
SIMZP1750.prop('checked', false);
SIMZP2000.prop('checked', false);
SIMZP2250.prop('checked', false);
SIMZP2500.prop('checked', false);
SIMZP3000.prop('checked', false);

    }
});

SIMBSMCB.on('click', function(){
    if($(this).is(':checked')){
        SIMZP.show();
        SIMZP1.hide();
        SIMZP2.hide();
        SIMZP3.hide();
        SIMZP4.hide();
        SIMZPCB.prop('checked', false);
        SIMZP400.prop('checked', false);
        SIMZP500.prop('checked', false);
        SIMZP750.prop('checked', false);
        SIMZP1000.prop('checked', false);
        SIMZP1250.prop('checked', false);
        SIMZP1500.prop('checked', false);
        SIMZP1750.prop('checked', false);
        SIMZP2000.prop('checked', false);
        SIMZP2250.prop('checked', false);
        SIMZP2500.prop('checked', false);
        SIMZP3000.prop('checked', false);
    } else {
        SIMZP.hide();
        SIMZP1.hide();
        SIMZP2.hide();
        SIMZP3.hide();
        SIMZP4.hide();
        SIMZPCB.prop('checked', false);
        SIMZP400.prop('checked', false);
        SIMZP500.prop('checked', false);
        SIMZP750.prop('checked', false);
        SIMZP1000.prop('checked', false);
        SIMZP1250.prop('checked', false);
        SIMZP1500.prop('checked', false);
        SIMZP1750.prop('checked', false);
        SIMZP2000.prop('checked', false);
        SIMZP2250.prop('checked', false);
        SIMZP2500.prop('checked', false);
        SIMZP3000.prop('checked', false);
    }
});

SIMZPCB.on('click', function(){
    if($(this).is(':checked')){
        SIMZP1.show();
        SIMZP2.show();
        SIMZP3.show();
        SIMZP4.show();
        SIMZP400.prop('checked', false);
        SIMZP500.prop('checked', false);
        SIMZP750.prop('checked', false);
        SIMZP1000.prop('checked', false);
        SIMZP1250.prop('checked', false);
        SIMZP1500.prop('checked', false);
        SIMZP1750.prop('checked', false);
        SIMZP2000.prop('checked', false);
        SIMZP2250.prop('checked', false);
        SIMZP2500.prop('checked', false);
        SIMZP3000.prop('checked', false);   
    } else {
        SIMZP1.hide();
        SIMZP2.hide();
        SIMZP3.hide();
        SIMZP4.hide();
        SIMZP400.prop('checked', false);
        SIMZP500.prop('checked', false);
        SIMZP750.prop('checked', false);
        SIMZP1000.prop('checked', false);
        SIMZP1250.prop('checked', false);
        SIMZP1500.prop('checked', false);
        SIMZP1750.prop('checked', false);
        SIMZP2000.prop('checked', false);
        SIMZP2250.prop('checked', false);
        SIMZP2500.prop('checked', false);
        SIMZP3000.prop('checked', false);
    }
});

SIMSMCB.on('click', function(){
    if($(this).is(':checked')){

SIMDB.show();
SIMDBALL.hide();

SIMSTQP.show();
SIMSTQPALL1.hide();
SIMSTQPALL2.hide();

SIMSMZP.show();
SIMSMZPALL.hide();

SIMDY.show();
SIMDY1.hide();
SIMDY2.hide();

SIMWP.show();
SIMWP1.hide();
SIMWP2.hide();
SIMWP3.hide();

SIMDBCB.prop('checked', false);
SIMDBWW.prop('checked', false);
SIMDBZZ.prop('checked', false);
SIMDBWZ.prop('checked', false);

SIMSTQPCB.prop('checked', false);
SIMSTQPTT.prop('checked', false);
SIMSTQPTAT.prop('checked', false);
SIMSTQPS.prop('checked', false);
SIMSTQPWT.prop('checked', false);

SIMSMZPCB.prop('checked', false);
SIMSMZPEE.prop('checked', false);
SIMSMZPMM.prop('checked', false);
SIMSMZPTT.prop('checked', false);

SIMDYCB.prop('checked', false);
SIMDYEE1.prop('checked', false);
SIMDYEE2.prop('checked', false);
SIMDYTT1.prop('checked', false);
SIMDYTT2.prop('checked', false);
SIMDYMM1.prop('checked', false);
SIMDYMM2.prop('checked', false);

SIMWPCB.prop('checked', false);
SIMWPEVB.prop('checked', false);
SIMWPEVBV.prop('checked', false);
SIMWPEVNBV.prop('checked', false);
SIMWPTVB.prop('checked', false);
SIMWPTVBV.prop('checked', false);
SIMWPTVNBV.prop('checked', false);
SIMWPWVB.prop('checked', false);
SIMWPWVBV.prop('checked', false);
SIMWPWVNBV.prop('checked', false);


    } else {

SIMDB.hide();
SIMDBALL.hide();

SIMSTQP.hide();
SIMSTQPALL1.hide();
SIMSTQPALL2.hide();

SIMSMZP.hide();
SIMSMZPALL.hide();

SIMDY.hide();
SIMDY1.hide();
SIMDY2.hide();

SIMWP.hide();
SIMWP1.hide();
SIMWP2.hide();
SIMWP3.hide();

SIMDBCB.prop('checked', false);
SIMDBWW.prop('checked', false);
SIMDBZZ.prop('checked', false);
SIMDBWZ.prop('checked', false);

SIMSTQPCB.prop('checked', false);
SIMSTQPTT.prop('checked', false);
SIMSTQPTAT.prop('checked', false);
SIMSTQPS.prop('checked', false);
SIMSTQPWT.prop('checked', false);

SIMSMZPCB.prop('checked', false);
SIMSMZPEE.prop('checked', false);
SIMSMZPMM.prop('checked', false);
SIMSMZPTT.prop('checked', false);

SIMDYCB.prop('checked', false);
SIMDYEE1.prop('checked', false);
SIMDYEE2.prop('checked', false);
SIMDYTT1.prop('checked', false);
SIMDYTT2.prop('checked', false);
SIMDYMM1.prop('checked', false);
SIMDYMM2.prop('checked', false);

SIMWPCB.prop('checked', false);
SIMWPEVB.prop('checked', false);
SIMWPEVBV.prop('checked', false);
SIMWPEVNBV.prop('checked', false);
SIMWPTVB.prop('checked', false);
SIMWPTVBV.prop('checked', false);
SIMWPTVNBV.prop('checked', false);
SIMWPWVB.prop('checked', false);
SIMWPWVBV.prop('checked', false);
SIMWPWVNBV.prop('checked', false);
    }
});

SIMDBCB.on('click', function(){
    if($(this).is(':checked')){
        SIMDBALL.show();
        SIMDBWW.prop('checked', false);
        SIMDBZZ.prop('checked', false);
        SIMDBWZ.prop('checked', false);
    } else {
        SIMDBALL.hide();
        SIMDBWW.prop('checked', false);
        SIMDBZZ.prop('checked', false);
        SIMDBWZ.prop('checked', false); 
    }
});

SIMSTQPCB.on('click', function(){
    if($(this).is(':checked')){
        SIMSTQPALL1.show();
        SIMSTQPALL2.show();
        SIMSTQPTT.prop('checked', false);
        SIMSTQPTAT.prop('checked', false);
        SIMSTQPS.prop('checked', false);
        SIMSTQPWT.prop('checked', false);
    } else {
        SIMSTQPALL1.hide();
        SIMSTQPALL2.hide();
        SIMSTQPTT.prop('checked', false);
        SIMSTQPTAT.prop('checked', false);
        SIMSTQPS.prop('checked', false);
        SIMSTQPWT.prop('checked', false);
    }
});

SIMSMZPCB.on('click', function(){
    if($(this).is(':checked')){
        SIMSMZPALL.show();
        SIMSMZPEE.prop('checked', false);
        SIMSMZPMM.prop('checked', false);
        SIMSMZPTT.prop('checked', false);
    } else {
        SIMSMZPALL.hide();
        SIMSMZPEE.prop('checked', false);
        SIMSMZPMM.prop('checked', false);
        SIMSMZPTT.prop('checked', false);
    }
});

SIMDYCB.on('click', function(){
    if($(this).is(':checked')){
        SIMDY1.show();
        SIMDY2.show();
        SIMDYEE1.prop('checked', false);
        SIMDYEE2.prop('checked', false);
        SIMDYTT1.prop('checked', false);
        SIMDYTT2.prop('checked', false);
        SIMDYMM1.prop('checked', false);
        SIMDYEE2.prop('checked', false);
    } else {
        SIMDY1.hide();
        SIMDY2.hide();
        SIMDYEE1.prop('checked', false);
        SIMDYEE2.prop('checked', false);
        SIMDYTT1.prop('checked', false);
        SIMDYTT2.prop('checked', false);
        SIMDYMM1.prop('checked', false);
        SIMDYEE2.prop('checked', false);
    }
});

SIMWPCB.on('click', function(){
    if($(this).is(':checked')){
        SIMWP1.show();
        SIMWP2.show();
        SIMWP3.show();
        SIMWPEVB.prop('checked', false);
        SIMWPEVBV.prop('checked', false);
        SIMWPEVNBV.prop('checked', false);
        SIMWPTVB.prop('checked', false);
        SIMWPTVBV.prop('checked', false);
        SIMWPTVNBV.prop('checked', false);
        SIMWPWVB.prop('checked', false);
        SIMWPWVBV.prop('checked', false);
        SIMWPWVNBV.prop('checked', false);
    } else {
        SIMWP1.hide();
        SIMWP2.hide();
        SIMWP3.hide();
        SIMWPEVB.prop('checked', false);
        SIMWPEVBV.prop('checked', false);
        SIMWPEVNBV.prop('checked', false);
        SIMWPTVB.prop('checked', false);
        SIMWPTVBV.prop('checked', false);
        SIMWPTVNBV.prop('checked', false);
        SIMWPWVB.prop('checked', false);
        SIMWPWVBV.prop('checked', false);
        SIMWPWVNBV.prop('checked', false);
    }
});

GO.on('click', function(){
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');

    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        } else {            
            headerText.html("Loading!");                                        
        }        
        form.classList.add('was-validated');
      }, false);
    });
});

$('#carouselExampleIndicators2').carousel({
interval: 20
});