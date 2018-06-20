var play;
var stop;
var select_element; 

// Update students when programme or branch is inputted
function update(){
	data = {
		'programme' : $("#programme").val(),
		'branch'    : $("#branch").val(),
	}
	$.post(update_url, data, function(data, textStatus, jqXHR){
		// Remove all old names from the student list
		$('#student').children('option').remove();
		// Add all new names
		for (i = 0; i < data.length; i++) {
			to_append = '<option value="' + data[i].id + '">' + data[i].name + '</option>'
			$("#student").append(to_append);
		}
	}, "json");
}

// Moves select element to next item
//	this is invoked in stop_handler
function goto_next(){
	var next = select_element.find(':selected').next()
	if(next.length==1)
	{
		select_element.val(next.val());
	} 
	else if(next.length==0)
	{
		if(select_element.attr('id')=='student')
			alert("Last item reached!")
	}
	else
	{
		console.log("Error - Length of next option should be either 0 or 1")
	}
}

function play_handler(){
	if(!play.hasClass('disabled')){
		data = {
			'referer' : window.location.pathname,
			'id' : select_element.val()
		}
		$.post( play_url, data, function(data, textStatus, jqXHR){
			console.log(data)
			play.addClass("disabled")
			stop.removeClass("disabled")
		});
	}
}

function stop_handler(){
	if(!stop.hasClass('disabled')){
		$.post( stop_url, {}, function(data, textStatus, jqXHR){
			console.log(data)
			goto_next()
			stop.addClass("disabled")
			play.removeClass("disabled")
		});
	}
}

$(document).ready(function(){
	// Init
	play = $("#play");
	stop = $("#stop");
	switch(window.location.pathname) {
		case "/convo20/dignitary/":
			select_element = $("#dignitary")
			break;		
		case "/convo20/medal/":
			select_element = $("#medal")
			break;		
		case "/convo20/student/":
			select_element = $("#student")
			break;
		default:
			console.log("Error - Switch case in default")
			return {}
	}

	// Play button AJAX
	play.click(play_handler);

	// Stop button AJAX
	stop.click(stop_handler);

	// Attach Handlers
	$('#programme').on('input', update); // Update students on programme input
	$('#branch').on('input', update); 	// Update students on branch input

	// Register Hotkeys for Play and Stop buttons
	select_element.bind('keydown', 'p', function(){play.click();});	
	select_element.bind('keydown', 's', function(){stop.click();});	
});