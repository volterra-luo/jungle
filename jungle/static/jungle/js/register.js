$( document ).ready( function(){
	
  $(':input').addClass("form-control");

	$(function(){
    var email = $('#id_email');
    var username = $(':text');
		var pwd = $(':password');

    email.hover(function(){
      $(this).attr('placeholder','somebody@awesome.com');
    });

    username.hover(function(){
      $(this).attr('placeholder','e.g. somebody');
    });

    pwd.hover(function(){
      $(this).attr('placeholder','e.g. top-secret');
    });
  });

  $('#termofuse').click(function(){
    if($(this).attr("checked")) {
      $('#submitB').attr("disabled",'disabled');
    		$(this).attr("checked", false)
   		}
   		else {
    		$('#submitB').attr("disabled", false);
    		$(this).attr("checked", true)
    	}
   	});
});
