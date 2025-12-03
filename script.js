// Smooth scroll animation for sections
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.section-title, .section-subtitle, .about-text, .about-image, .feature-card, .project-card, .cta-content, .contact-card, .contact-form').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});

// Hero grid zoom-out effect on scroll with scroll locking
const heroGrid = document.getElementById('heroGrid');
const heroSection = document.getElementById('home');
const heroContent = document.querySelector('.hero-content');
let scrollAccumulator = 0;
let isZoomComplete = false;
const maxScroll = 2000; // Scroll distance needed to complete zoom
const scrollBuffer = 200; // Extra scroll needed after animation completes
const totalScrollNeeded = maxScroll + scrollBuffer; // 2200 total

console.log('Hero grid element:', heroGrid);
console.log('Hero section:', heroSection);
console.log('Hero content:', heroContent);

// Prevent actual page scroll until zoom completes
window.addEventListener('wheel', (e) => {
    // Handle zoom effect when at top of page
    if (window.scrollY < 100) {
        // Check if scrolling down and not reached buffer limit
        if (e.deltaY > 0 && scrollAccumulator < totalScrollNeeded) {
            e.preventDefault();
            isZoomComplete = false;
        }
        // Check if scrolling up and zoom accumulator is active
        else if (e.deltaY < 0 && scrollAccumulator > 0) {
            e.preventDefault();
            isZoomComplete = false;
        }

        // Accumulate scroll (both directions)
        scrollAccumulator += e.deltaY;
        scrollAccumulator = Math.max(0, Math.min(scrollAccumulator, totalScrollNeeded));

        // Calculate scale based on accumulated scroll
        // Cap the scroll percent at 1 so scale stays locked at 0.33 during buffer
        const scrollPercent = Math.min(scrollAccumulator / maxScroll, 1);
        const scale = 1 - (scrollPercent * 0.67); // 1 to 0.33 (reveals all 9 images)

        heroGrid.style.transform = `translate(-50%, -50%) scale(${scale})`;

        // Fade out hero content as animation starts
        // Start fading immediately (at 0), fully faded by 60% of animation
        const fadeEnd = maxScroll * 0.6; // Fully faded at 1200

        if (scrollAccumulator <= 0) {
            heroContent.style.opacity = '1';
        } else if (scrollAccumulator >= fadeEnd) {
            heroContent.style.opacity = '0';
        } else {
            const fadeProgress = scrollAccumulator / fadeEnd;
            heroContent.style.opacity = (1 - fadeProgress).toString();
        }

        // Log status
        if (scrollAccumulator > maxScroll) {
            console.log('Buffer period - Scroll:', scrollAccumulator, 'Scale locked at:', scale.toFixed(2));
        } else {
            console.log('Animating - Scroll:', scrollAccumulator, 'Scale:', scale.toFixed(2));
        }

        // Only allow scrolling when animation is 100% complete AND buffer reached
        if (scale <= 0.34 && e.deltaY > 0 && scrollAccumulator >= totalScrollNeeded) {
            // Animation complete + buffer reached, allow normal scrolling
            isZoomComplete = true;
            console.log('Zoom complete! Normal scrolling enabled at:', scrollAccumulator);
        } else if (e.deltaY > 0 && !isZoomComplete) {
            // Still in locked state, prevent scroll
            e.preventDefault();
        }

        // When zoomed back in completely
        if (scrollAccumulator <= 0 && e.deltaY < 0) {
            console.log('Fully zoomed in!');
        }
    }
    // If scrolled down the page and scrolling back up, re-enable zoom effect
    else if (window.scrollY > 0 && e.deltaY < 0 && window.scrollY < 200) {
        // Reset when scrolling back to top
        if (scrollAccumulator >= maxScroll) {
            isZoomComplete = false;
        }
    }
}, { passive: false });

// Regular scroll handler for navbar
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Set initial transform (shows center image only)
console.log('Setting initial transform');
heroGrid.style.transform = 'translate(-50%, -50%) scale(1)';

// Split nav links into letter spans for animation
document.querySelectorAll('.nav-links a').forEach(link => {
    const text = link.textContent;
    link.textContent = '';

    text.split('').forEach((letter, index) => {
        const span = document.createElement('span');
        // Preserve spaces as non-breaking spaces
        span.innerHTML = letter === ' ' ? '&nbsp;' : letter;
        span.style.animationDelay = `${index * 0.05}s`;
        link.appendChild(span);
    });
});

// Project filtering functionality
const filterButtons = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');

        // Get the filter value
        const filterValue = button.getAttribute('data-filter');

        // Filter projects
        projectCards.forEach(card => {
            const category = card.getAttribute('data-category');

            if (filterValue === 'all' || category === filterValue) {
                // Show the card with animation
                card.style.display = 'flex';
                setTimeout(() => {
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0) scale(1)';
                }, 10);
            } else {
                // Hide the card with animation
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px) scale(0.95)';
                setTimeout(() => {
                    card.style.display = 'none';
                }, 300);
            }
        });
    });
});

// Metrics Animation
const metrics = document.querySelectorAll('.metric .num');
let animated = false;

const animateMetrics = () => {
    metrics.forEach(metric => {
        const target = metric.innerText;
        const isPercentage = target.includes('%');
        const isPlus = target.includes('+');
        const value = parseInt(target.replace(/[^0-9]/g, ''));

        let current = 0;
        const increment = Math.ceil(value / 50); // Speed of animation
        const timer = setInterval(() => {
            current += increment;
            if (current >= value) {
                current = value;
                clearInterval(timer);
            }
            metric.innerText = current + (isPlus ? '+' : '') + (isPercentage ? '%' : '');
        }, 40);
    });
};

const metricsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
            animateMetrics();
            animated = true;
        }
    });
}, { threshold: 0.5 });

const metricsSection = document.querySelector('.metrics');
if (metricsSection) {
    metricsObserver.observe(metricsSection);
}

// Contact Form Simulation
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = contactForm.querySelector('button[type="submit"]');
        const originalText = btn.innerText;

        // Change button state
        btn.innerText = 'Versturen...';
        btn.disabled = true;
        btn.style.opacity = '0.7';

        // Send data to Formspree
        const formData = new FormData(contactForm);

        // Gebruik de URL die in de HTML action staat
        fetch(contactForm.action, {
            method: "POST",
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        }).then(response => {
            if (response.ok) {
                // Success handling
                btn.innerText = originalText;
                btn.disabled = false;
                btn.style.opacity = '1';

                // Show success message
                let successMsg = contactForm.querySelector('.form-success');
                if (!successMsg) {
                    successMsg = document.createElement('div');
                    successMsg.className = 'form-success';
                    successMsg.innerText = 'Bedankt voor je bericht! Ik neem zo snel mogelijk contact op.';
                    contactForm.insertBefore(successMsg, contactForm.querySelector('.contact-actions'));
                }
                successMsg.style.display = 'block';
                successMsg.style.backgroundColor = 'rgba(16, 185, 129, 0.1)';
                successMsg.style.color = '#10b981';
                contactForm.reset();

                // Hide success message after 5 seconds
                setTimeout(() => {
                    successMsg.style.display = 'none';
                }, 5000);
            } else {
                // Error handling
                response.json().then(data => {
                    if (Object.hasOwn(data, 'errors')) {
                        alert(data["errors"].map(error => error["message"]).join(", "));
                    } else {
                        alert("Oeps! Er is iets misgegaan bij het versturen van je bericht.");
                    }
                });
                btn.innerText = originalText;
                btn.disabled = false;
                btn.style.opacity = '1';
            }
        }).catch(error => {
            alert("Oeps! Er is een probleem met het versturen.");
            btn.innerText = originalText;
            btn.disabled = false;
            btn.style.opacity = '1';
        });
    });
}

// Dynamic Year
document.getElementById('year').innerText = new Date().getFullYear();
