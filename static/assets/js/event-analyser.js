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
interval: 100
});