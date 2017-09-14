var go = true;

var window_width = $(window).width();

$(document).ready(function(){
	//scroll scan for header bar


    if(window_width > 768){

	$(window).scroll( function() {
    	    var top = $(this).scrollTop();
    	    if ( top > 80 && go) {
                go = false;
    		$(".h-change").stop().animate({
                    'line-height': "40px"
                });
                $('#header-bar').stop().animate({
                    backgroundColor: "rgb(44, 47, 59)"
                });
                $('.user-drop').animate({
                    backgroundColor: "rgb(44, 47, 59)",
                });
            }
    	
            if (top < 60 && !go) {
                go = true;
                $(".h-change").stop().animate({
                    'line-height': "30px"
                });
                $('#header-bar').stop().animate({
                    backgroundColor: "transparent"
                });
                $('.user-drop').animate({
                    backgroundColor: "transparent",
                });
                
    	   }
    	});
    } else{

    	$(".h-change").stop().animate({
                    'line-height': "40px"
                });
                $('#header-bar').stop().animate({
                    backgroundColor: "rgb(44, 47, 59)"
                });
                $('.user-drop').animate({
                    backgroundColor: "rgb(44, 47, 59)",
                });
    }

	$('body').scrollspy({ target: '#header-navbar' });

    $('.h3-title').hover(
            function() {
                $( this ).children(".title-arrow").stop(true, true).show("slide", { direction: "right" }, 300);
            }, function() {
                $( this ).children(".title-arrow").stop(true, true).hide("slide", { direction: "right" }, 300);
            });

    $('.small-title').hover(
        function(){
            $(this).children(".title-after").show();
            $(this).children(".title-after").stop().animate({
                opacity: 1,
                top: "25%"
            },{duration: 300});

        },function(){
            $(this).children(".title-after").hide();
            $(this).children(".title-after").stop().animate({
                opacity: 0,
                top: "100%"
            },{duration: 300});

        });

});

