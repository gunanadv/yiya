$(document).ready(function(){
	//scroll scan for header bar

    $(".number").keydown(function(event) {
        // Allow: backspace, delete, tab, escape, and enter
        if ( event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 || event.keyCode == 13 || 
             // Allow: Ctrl+A
            (event.keyCode == 65 && event.ctrlKey === true) || 
            // Allow: home, end, left, right
            (event.keyCode >= 35 && event.keyCode <= 39)) {
             // let it happen, don't do anything
                return;
        }
        else {
            // Ensure that it is a number and stop the keypress
            if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault(); 
            }   
        }
    });


    $(".date_picker").datepicker({ dateFormat: 'yy-mm-dd' ,      
    						changeMonth: true,
           					changeYear: true});

    $("#id_gender li").first().addClass("hide");

     setTimeout(function(){$('#application-submit-success').hide("slide", { direction: "up" }, 300)}, 3000);

});
