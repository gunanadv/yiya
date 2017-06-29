$(document).ready(function(){

    $('#forget-password-submit').click(function(){

    	$("#forget-password-success").hide();
    	$("#forget-password-fail").hide();

    	$(this).prop("disabled",true);

        input_data = {"email" : $("#input-email").val(),}

        $.ajax({
            type: "POST",
            url: "/forget-password-submit/",
            dataType: "json",
            data: input_data,
            success: function(data) {
                if(data.message == 'success'){
                    $("#forget-password-success").slideDown("slow");
                    $("#forget-password-submit").hide();
                }
                else
                    $("#forget-password-fail").slideDown("slow");
                    $('#forget-password-submit').removeAttr("disabled");
            },
            error: function(data) {
                $("#forget-password-fail").slideDown("slow");
                $('#forget-password-submit').removeAttr("disabled");
            }
        });

    });


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
});