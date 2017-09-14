$(document).ready(function(){

    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 


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

    $('.service-select').click(function() {
        $('#input-service').val($(this).text());
    });


    $('.trigger-hide').click(function(){
        $(".c-input").popover('hide');
    });

    $('.modal-trigger').click(function(){
        $(".c-input").popover('hide');
        $("#consultation-success").hide();
        $("#consultation-fail").hide();
        $("#consultation-submit").show();
    });

    $(function () {
        $('.c-input').popover({placement : 'top', content: '请输入这一栏。', trigger: 'manual' });
        $('.vip-style').popover({trigger: 'hover' });
    })
   

    function consultation_check(){

        if(!$("#input-name").val()){
            $("#input-name").popover('show');
            return false;
        }else{
            $("#input-name").popover('hide');
        }

        if(!$("#input-email").val()){
            $("#input-email").popover('show');
            return false;
        }else{
            $("#input-email").popover('hide');
        }

        if(!$("#input-service").val()){
            $("#input-service").popover('show');
            return false;
        }else{
            $("#input-service").popover('hide');
        }

        return true;

    }

    $('#consultation-submit').click(function(){

    	$("#consultation-fail").hide();
    	$("#consultation-success").hide();

        if(!consultation_check()){
            return;
        }

        $(this).prop("disabled",true);
        $(this).html("提交中....");

        input_data = {"name" : $("#input-name").val(),
                "email" : $("#input-email").val(),
                "phone" : $("#input-phone").val(),
                "description" : $("#c-description").val(),
                "service" : $("#input-service").val()}

        $.ajax({
            type: "POST",
            url: "/consultation-submit/",
            dataType: "json",
            data: input_data,
            success: function(data) {
                if(data.message == 'success'){
                    $("#consultation-success").slideDown("slow");
                    $("#consultation-submit").hide();
                    $('#consultation-submit').removeAttr("disabled");
                    $('#consultation-submit').html("提交咨询");
                }
                else
                    $("#consultation-fail").slideDown("slow");
                    $('#consultation-submit').removeAttr("disabled");
                    $('#consultation-submit').html("提交咨询");
            },
            error: function(data) {
                $("#consultation-fail").slideDown("slow");
                $('#consultation-submit').removeAttr("disabled");
                $('#consultation-submit').html("提交咨询");
            }
        });

    });


});