var play;
var stop;





function goto_next(){
	var next = $('#medal').find(':selected').next()
	if(next.length==1)
	{
		$('#medal').val(next.val());
	} 
	else if(next.length==0)
	{
		alert("Last item reached!")
	}
	else
	{
		console.log("Error - Length of next option should be either 0 or 1")
	}
}



$(document).ready(function(){
	// console.log("Hello")

	play = $("#play");
	stop = $("#stop");

	play.click(function(){
		if(!play.hasClass('disabled')){
			// console.log("Play Clicked")
			data = {
			'id'        : 'student'
			'medal_name'   : $("#medal").val().split(", ")[0],
			}
			$.post( play_url, data, function(data, textStatus, jqXHR){
				console.log(data)
				play.addClass("disabled")
				stop.removeClass("disabled")
			});
		}
	});

	stop.click(function(){
		if(!stop.hasClass('disabled')){
			// console.log("Stop Clicked")
			$.post( stop_url, data, function(data, textStatus, jqXHR){
				console.log(data)
				goto_next()
				stop.addClass("disabled")
				play.removeClass("disabled")
			});
		}
	});


	$(document).bind('keydown', 'ctrl+[', function(){
		play.click();
	});	
	$(document).bind('keydown', 'ctrl+]', function(){
		stop.click();
	});	
});