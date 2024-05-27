// Select the rotated border element
const rotatedBorder = document.querySelector('.rotated-border');

// Add an event listener to the window's scroll event
window.addEventListener('scroll', function() {
  // Calculate the rotation angle based on the scroll position
  const rotationAngle = window.scrollY / 9 + 75; // Adjust the divisor to control the rotation speed
  
  // Apply the rotation transformation to the rotated border element
  rotatedBorder.style.transform = `rotate(${rotationAngle}deg)`;
});


document.querySelector('.prev-btn').addEventListener('click', function() {
  document.querySelector('.slider-container').scrollBy({
    left: -100, // Adjust scroll amount
    behavior: 'smooth'
  });
});

document.querySelector('.next-btn').addEventListener('click', function() {
  document.querySelector('.slider-container').scrollBy({
    left: 100, // Adjust scroll amount
    behavior: 'smooth'
  });
});

// email js

