function toggleMenu() {
    const nav = document.getElementById('nav');
    if (nav.style.display === "none" || nav.style.display === "") {
        nav.style.display = "flex";
    } else {
        nav.style.display = "none";
    }
}

// Function to check if the device is a mobile
function isMobile() {
    return window.innerWidth <= 768; // You can adjust this value as needed
}

// Get all the anchor tags within the navigation menu
const navLinks = document.querySelectorAll('#nav a');

// Add click event listeners to each anchor tag
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        // Check if the device is mobile, then hide the navigation menu
        if (isMobile()) {
            const nav = document.getElementById('nav');
            nav.style.display = "none";
        }
    });
});

// Add event listener for window resize to handle changes in device width
window.addEventListener('resize', () => {
    // If the device is no longer mobile, ensure the navigation menu is visible
    if (!isMobile()) {
        const nav = document.getElementById('nav');
        nav.style.display = "flex";
    }
});
