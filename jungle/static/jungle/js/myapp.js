$( document ).ready( function() {
	var node = $('#spinning-container').children(0);
	var startDeg = random(360);
	var timer;

	node.css('background', 'none');
	node.css({
        top: random(40),
        left: random(10),
        zIndex: 1000
      }).hover(
          function() {
            node.fadeTo(250, 1)
                .css('zIndex', 1001)
                .css('transform', 'rotate(' + random(360) + 'deg)');
          },
          function() {
            node.fadeTo(250, .6).css('zIndex', 1000);
            timer && clearTimeout(timer);
            timer = setTimeout(spin, Math.ceil(random(1000)));
            //setInterval(spin, Math.ceil(random(10000)));
          }
     	);
    
    function spin() {
        node.css('transform', 'rotate(0deg)');
    }

	// node.on('mouseover', function(event){
	// 	console.log(random(10));
	// });

	function random(x) { return Math.random() * x };

      $('#id_captcha:text').addClass("form-control");
});