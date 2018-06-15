var play;
var stop;





function update_students(){
	// console.log( this.value );
	data = {
		'programme' : $("#programme").val(),
		'branch'    : $("#branch").val(),
	}
	$.post(update_url, data, function(data, textStatus, jqXHR){
		// Remove all old names from the student list
		$('#student').children('option').remove();
		// Add all new names
		for (i = 0; i < data.length; i++) {
			to_append = '<option value="' + data[i] + '">' + data[i] + '</option>'
			$("#student").append(to_append);
		}
	}, "json");
}





function goto_next(){
	var next = $('#student').find(':selected').next()
	if(next.length==1)
	{
		$('#student').val(next.val());
	} 
	else if(next.length==0)
	{
		alert("Last Element Reached!")
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
		// console.log("Play Clicked")
		data = {
		'programme' : $("#programme").val(),
		'branch'    : $("#branch").val(),
		'student'   : $("#student").val()
		}
		$.post( play_url, data, function(data, textStatus, jqXHR){
			console.log(data)
		});
	});

	stop.click(function(){
		// console.log("Stop Clicked")
		$.post( stop_url, data, function(data, textStatus, jqXHR){
			console.log(data)
			goto_next()
		});
	});

	$('#programme').on('input', update_students)
	$('#branch').on('change', update_students)

});