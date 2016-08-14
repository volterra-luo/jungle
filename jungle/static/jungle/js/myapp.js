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
            setInterval(spin, Math.ceil(random(10000)));
          }
     	);
    
    function spin() {
        node.css('transform', 'rotate(' + random(360) + 'deg)');
    }

	// node.on('mouseover', function(event){
	// 	console.log(random(10));
	// });

    function random(x) { return Math.random() * x };

    setInterval(changebitadrress, 3000);
    

    function changebitadrress() { 
      var s = $("#bitcoin-address").html();
      $("#bitcoin-address").html(s.changeCode());
    };
    
    
    String.prototype.changeCode = function() {
      if (this.length === 0) return '';
      var l = shuffle(this.trim().split(''));
      return l.join('');
    };

    function shuffle(array) {
      var currentIndex = array.length, temporaryValue, randomIndex;

      while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
      }

      return array;
    };
});