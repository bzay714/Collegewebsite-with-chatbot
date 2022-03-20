scroll_button = document.querySelector('.gotopbtn')


var myScrollFunc = function() {
    var y = window.scrollY;
    if (y >= 300) {
        scroll_button.className = "gotopbtn show"
    } else {
        scroll_button.className = "gotopbtn hide"
    }
  };


  window.addEventListener("scroll", myScrollFunc);