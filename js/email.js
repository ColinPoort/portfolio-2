document.addEventListener("DOMContentLoaded", function () {
    try {
      emailjs.init("LFhKlHMi6qymIV-YK"); // Replace 'YOUR_USER_ID' with your actual user ID from EmailJS
      console.log("EmailJS initialized");
    } catch (error) {
      console.error("Error initializing EmailJS:", error);
      return;
    }
  
    var contactForm = document.getElementById("contact-form");
    if (contactForm) {
      console.log("Contact form found");
      contactForm.addEventListener("submit", function (event) {
        event.preventDefault();
        console.log("Form submit event triggered");
  
        const alertBox = document.getElementById("alert");
  
        emailjs.sendForm("service_ydjnkmh", "template_ko7fg0a", contactForm).then(
          function () {
            alertBox.textContent = "Email sent successfully!";
            alertBox.className = "alert alert-success show";
            alertBox.style.display = "block"; // Ensure the alert box is visible
            setTimeout(() => {
              alertBox.classList.remove("show");
              setTimeout(() => {
                alertBox.style.display = "none"; // Hide the alert box after transition ends
              }, 500); // Match the transition duration in CSS
            }, 5000); // Hide after 5 seconds
            contactForm.reset(); // Reset the form
          },
          function (error) {
            alertBox.textContent =
              "Failed to send email: " + JSON.stringify(error);
            alertBox.className = "alert alert-error show";
            alertBox.style.display = "block"; // Ensure the alert box is visible
            setTimeout(() => {
              alertBox.classList.remove("show");
              setTimeout(() => {
                alertBox.style.display = "none"; // Hide the alert box after transition ends
              }, 500); // Match the transition duration in CSS
            }, 5000); // Hide after 5 seconds
          }
        ).catch(function(error) {
          console.error("EmailJS sendForm error:", error);
        });
      });
    } else {
      console.error("Form with id 'contact-form' not found");
    }
  });