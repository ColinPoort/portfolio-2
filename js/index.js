// Select the rotated border element
const rotatedBorder = document.querySelector('.rotated-border');

// Add an event listener to the window's scroll event
window.addEventListener('scroll', function() {
  // Calculate the rotation angle based on the scroll position
  const rotationAngle = window.scrollY / 9 + 75; // Adjust the divisor to control the rotation speed
  
  // Apply the rotation transformation to the rotated border element
  rotatedBorder.style.transform = `rotate(${rotationAngle}deg)`;
});


