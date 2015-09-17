$( document ).ready( function(){
	$(':input').addClass("form-control");

	$(function(){
    	var username = $(':text');
		var pwd = $(':password');
    		username.hover(function(){
      			$(this).attr('placeholder','e.g. test');
    		});
		pwd.hover(function(){
			$(this).attr('placeholder','e.g. 123456');
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
