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

    setTimeout(function(){$('#selfi-submit-success').hide("slide", { direction: "up" }, 300)}, 3000);

    $('#application-create').click(function(){
    	isreload = false;

    	if($("#student-id").length) {

        input_data = {"application_name" : $("#id_application_name").val(),
                "application_type" : $("#id_application_type").val(),
                "application_email" : $("#id_application_email").val(),
                "fee" : $("#id_fee").val(),
                "stage" : $("#id_stage").val(),
                "student_id" : $("#student-id").val(),
             };
             isreload = true;
         }
         else {

         	input_data = {"application_name" : $("#id_application_name").val(),
                "application_type" : $("#id_application_type").val(),
                "application_email" : $("#id_application_email").val(),
                "fee" : $("#id_fee").val(),
                "stage" : $("#id_stage").val()
             };
             isreload = false;
         }

        $.ajax({
            type: "POST",
            url: "/application-create-submit/",
            dataType: "json",
            data: input_data,
            success: function(data) {
            	if(isreload)
               		location.reload();
               	else{
               		if(data.message == 'success'){
               			$("#application-create-box").addClass("alert-success");
               			$("#application-create-message").html(data.url);
               			$("#application-create-box").show();
               		}
               		if(data.message == 'fail'){
               			$("#application-create-box").addClass("alert-danger");
               			$("#application-create-message").html(data.errors);
               			$("#application-create-box").show();
               		}
               	}
            }
        });

    });


    $('#new-password-submit').click(function(){

        input_data = {"old_password" : $("#old-password").val(),
        			   "new_password" : $("#new-password").val(),};

        $.ajax({
            type: "POST",
            url: "/new-password-submit/",
            dataType: "json",
            data: input_data,
            success: function(data) {
                if(data.message == 'success'){
                    $("#password-success").slideDown("slow");
                    $("#password-submit").hide();
                }
                else
                    $("#password-fail").slideDown("slow");
            },
            error: function(data) {
                $("#password-fail").slideDown("slow");
            }
        });

    });


});
