
$( "document").ready(function(){

	$("button").click(function() {
        $('html, body').animate({
            scrollTop: $("html").offset().top + 100
        }, 1000);
    });

	$(".btn2form").click(function() {
        $('html, body').animate({
            scrollTop: $("#form").offset().top + 100
        }, 1000);
    });

	$("#btn2front").click(function() {
        $('html, body').animate({
            scrollTop: $("#two").offset().top + 100
        }, 1000);
    });

$("#btn2droid").click(function() {
        $('html, body').animate({
            scrollTop: $("#three").offset().top + 100
        }, 2000);
    });

$("#btn2py").click(function() {
        $('html, body').animate({
            scrollTop: $("#four").offset().top + 100
        }, 2000);
    });

});

$( window ).scroll(function(){
	var wScroll = $(this).scrollTop();

	if(wScroll > $( "#two" ).offset().top - 250) {
		$("#two img").addClass("visible").delay(100).addClass("animated fadeInLeft");
		$("#two h2, #two p").addClass("visible").delay(100).addClass("animated fadeInDown");
		$("#two a").addClass("visible").delay(100).addClass("animated fadeIn");
	}

	if(wScroll > $( "#three" ).offset().top - 250) {
		$("#three img").addClass("visible").delay(100).addClass("animated fadeInLeft");
		$("#three h2, #three p").addClass("visible").delay(100).addClass("animated fadeInDown");
		$("#three a").addClass("visible").delay(100).addClass("animated fadeIn");
	}

	if(wScroll > $( "#four" ).offset().top- 250) {
		$("#four img").addClass("visible").delay(100).addClass("animated fadeInLeft");
		$("#four h2, #four p").addClass("visible").delay(100).addClass("animated fadeInDown");
		$("#four a").addClass("visible").delay(100).addClass("animated fadeIn");
	}

	if(wScroll > $( "#five" ).offset().top- 250) {
		$("#five img").addClass("visible").delay(100).addClass("animated fadeInUp");
		$("#five h2").addClass("visible").delay(100).addClass("animated fadeInDown");
	}

	if(wScroll > $( "#form" ).offset().top- 250) {
		$("#form h2").addClass("visible").delay(100).addClass("animated fadeInLeft");
		$("#form label").addClass("visible").addClass("animated fadeIn");
		$("#form input").addClass("visible").addClass("animated fadeIn");
		$("#form select").addClass("visible").addClass("animated fadeIn");
		}
});