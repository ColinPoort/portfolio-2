var prevScrollpos = window.pageYOffset;
var isMobile = window.matchMedia("(max-width: 768px)").matches;

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  var navbar = document.getElementById("navbar");

  if (isMobile) {
    if (prevScrollpos > currentScrollPos) {
      navbar.style.top = "0";
    } else {
      navbar.style.top = "-" + navbar.offsetHeight + "px";
    }
  }
  prevScrollpos = currentScrollPos;
}
