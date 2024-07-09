document.addEventListener('DOMContentLoaded', function() {
    gsap.registerPlugin(ScrollTrigger);
  
    // Animation for Home Section
    let tlHome = gsap.timeline({
      scrollTrigger: {
        trigger: '#home',
        start: 'top 80%',
        end: 'top 30%',
        toggleActions: 'play none none reverse'
      }
    });
    tlHome.from('.home hr', { y: -200, opacity: 0, duration: 0.6 })
          .from('.home h3', { x: -200, opacity: 0, duration: 0.6 }, '-=0.2')
          .from('.home p', { x: -200, opacity: 0, duration: 0.5 }, '-=0.1')
          .from('.box img', { x: 200, opacity: 0, duration: 0.6 }, '-=1')
          .from('.container .rotated-border', { x: -200, opacity: 0, duration: 0.5 }, '-=0.3')
          .from('.box-text', { x: -200, opacity: 0, duration: 0.7 }, '-=0.3')
          .from('.box-text h2', { x: -200, opacity: 0, duration: 0.5 }, '-=0.3')
          .from('.box-text h1', { x: -200, opacity: 0, duration: 1 }, '-=0.3')
          .from('.box-text p', { x: -200, opacity: 0, duration: 1.5 }, '-=0.5')
          .from('.cv', { x: -200, opacity: 0, duration: 0.5 }, '-=1');
  
    // Animation for About Section
    let tlAbout = gsap.timeline({
      scrollTrigger: {
        trigger: '#about',
        start: 'top 80%',
        end: 'top 30%',
        toggleActions: 'play none none reverse'
      }
    });
    tlAbout.from('.box-choose h1', { y: -200, opacity: 0, duration: 0.6 })
           .from('.column img', { x: -200, opacity: 0, duration: 0.6, stagger: 0.2 }, '-=0.4')
           .from('.column p', { x: 200, opacity: 0, duration: 0.7, stagger: 0.5 }, '-=0.4');
  
    // Animation for Learn More Section
    let tlLearnMore = gsap.timeline({
      scrollTrigger: {
        trigger: '.about',
        start: 'top 80%',
        end: 'top 30%',
        toggleActions: 'play none none reverse'
      }
    });
    tlLearnMore.from('.text-content h1', { x: -200, opacity: 0, duration: 0.6 })
               .from('.text-content p', { x: -200, opacity: 0, duration: 0.6 }, '-=0.3')
               .from('.about-image', { x: 200, opacity: 0, duration: 0.1, stagger: 0.3 }, '-=0.3');
  
    // Animation for Projects Section
    let tlProjects = gsap.timeline({
      scrollTrigger: {
        trigger: '#projects',
        start: 'top 80%',
        end: 'top 30%',
        toggleActions: 'play none none reverse'
      }
    });
    tlProjects.from('.project-title h1', { y: -200, opacity: 0, duration: 0.6 })
             .from('.carousel-cell', { y: 200, opacity: 0, duration: 0.6, stagger: 0.3 }, '-=0.4');
  
    // Animation for Contact Section
    let tlContact = gsap.timeline({
      scrollTrigger: {
        trigger: '.container-contact',
        start: 'top 80%',
        end: 'top 30%',
        toggleActions: 'play none none reverse'
      }
    });
    tlContact.from('.box1',{x: -200, opacity: 0, duration: 1})
            .from('.box1 h2', { y: -200, opacity: 0, duration: 0.6 },'-=0.5')
            .from('.box1 p', { x: -200, opacity: 0, duration: 0.4, stagger: 0.3 },'-=0.5')
            .from('.contact-form', { y: 200, opacity: 0, duration: 0.6 }, '-=1')
            .from('.form-group label',{x:70, opacity: 0, duration: 0.4, stagger: 0.2}, '-=0.6')
            .from('.form-group input, textarea',{x:-30, opacity: 0, duration: 0.5, stagger: 0.2}, '-=0,8')
            .from('.form-group button',{y:30, opacity: 0, duration: 0.2,}, '-=0,8')
             .from('.box2 h2', { y: -200, opacity: 0, duration: 0.6 }, '-=0.3')
             .from('.box2', { x: 200, opacity: 0, duration: 0.6 }, '-=0.3')
             .from('.box2 h1', { x: -60, opacity: 0, duration: 0.6 },'-=0.5')
             .from('.box2 p', { x: -200, opacity: 0, duration: 0.4, stagger: 0.3 },'-=0.5');
            
  
    // Animation for Footer Section
    let tlFooter = gsap.timeline({
      scrollTrigger: {
        trigger: '.container-contact',
        start: 'top 80%',
        end: 'top 30%',
        toggleActions: 'play none none reverse'
      }
    });
    tlFooter.from('footer p', { x: -200, opacity: 0, duration: 1 })
            .from('.social a', { x: 100, opacity: 0, duration: 0.7, stagger: 0.2 }, '-=0.3');
  
    // Function to reset all timelines on scroll up
    function resetTimelines() {
      tlHome.scrollTrigger.kill();
      tlAbout.scrollTrigger.kill();
      tlLearnMore.scrollTrigger.kill();
      tlProjects.scrollTrigger.kill();
      tlContact.scrollTrigger.kill();
      tlFooter.scrollTrigger.kill();
  
      tlHome = createTimeline('#home');
      tlAbout = createTimeline('#about');
      tlLearnMore = createTimeline('.about');
      tlProjects = createTimeline('#projects');
      tlContact = createTimeline('.container-contact');
      tlFooter = createTimeline('footer');
    }
  
    // Scroll event listener to reset timelines on scroll up
    window.addEventListener('scroll', function() {
      if (window.scrollY < document.querySelector('#home').offsetTop) {
        resetTimelines();
      }
    });
  
    // Function to create timeline with common configuration
    function createTimeline(trigger) {
      return gsap.timeline({
        scrollTrigger: {
          trigger: trigger,
          start: 'top 80%',
          end: 'top 30%',
          toggleActions: 'play none none reverse'
        }
      });
    }
  });
  