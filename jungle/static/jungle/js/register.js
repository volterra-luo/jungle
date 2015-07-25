$( document ).ready( function(){
	$(':input').addClass("form-control");

	$(function(){
    		var username = $(':text');
		var pwd = $(':password');
    		username.hover(function(){
      			$(this).attr('placeholder','test');
    		});
		pwd.hover(function(){
			$(this).attr('placeholder','123456');
		});
   	});

});
