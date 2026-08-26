/**
 * AETHER JEWELS – GSAP & ScrollTrigger Luxury Animations
 */

document.addEventListener('DOMContentLoaded', () => {
  if (typeof gsap === 'undefined') return;

  // Register ScrollTrigger plugin
  if (typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
  }

  // 1. CUSTOM STARDUST CURSOR PHYSICS
  const cursorDot = document.querySelector('.custom-cursor-dot');
  const cursorRing = document.querySelector('.custom-cursor-ring');

  if (cursorDot && cursorRing && window.innerWidth > 992) {
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let ringX = mouseX;
    let ringY = mouseY;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      gsap.to(cursorDot, { x: mouseX, y: mouseY, duration: 0.05, ease: 'power2.out' });
    });

    // Smooth ring lerp
    gsap.ticker.add(() => {
      ringX += (mouseX - ringX) * 0.15;
      ringY += (mouseY - ringY) * 0.15;
      gsap.set(cursorRing, { x: ringX, y: ringY });
    });

    // Hover expansions on interactive elements
    const interactiveElements = document.querySelectorAll('a, button, .btn, .product-card, .showcase-card, .config-option-card, input, select');
    interactiveElements.forEach((el) => {
      el.addEventListener('mouseenter', () => cursorRing.classList.add('active'));
      el.addEventListener('mouseleave', () => cursorRing.classList.remove('active'));
    });
  }

  // 2. HERO TIMELINE ANIMATION
  const heroTl = gsap.timeline({ defaults: { ease: 'power3.out' } });

  if (document.querySelector('.hero-section')) {
    heroTl
      .from('.hero-badge', { opacity: 0, y: -20, duration: 1, delay: 0.2 })
      .from('.hero-title', { opacity: 0, y: 40, duration: 1.2 }, '-=0.6')
      .from('.hero-tagline', { opacity: 0, y: 25, duration: 1 }, '-=0.8')
      .from('.hero-actions', { opacity: 0, y: 20, duration: 0.8 }, '-=0.6')
      .from('.hero-floating-jewel', { opacity: 0, scale: 0.85, duration: 1.4, ease: 'power2.out' }, '-=0.8')
      .from('.hero-scroll-indicator', { opacity: 0, duration: 1 }, '-=0.4');
  }

  // 3. PINNED HORIZONTAL SCROLL PRODUCT SHOWCASE
  const horizontalSection = document.querySelector('.horizontal-scroll-section');
  const horizontalTrack = document.querySelector('.horizontal-scroll-wrapper');

  if (horizontalSection && horizontalTrack && window.innerWidth > 992) {
    const totalScrollWidth = horizontalTrack.scrollWidth - window.innerWidth + 120;

    gsap.to(horizontalTrack, {
      x: () => -totalScrollWidth,
      ease: 'none',
      scrollTrigger: {
        trigger: horizontalSection,
        pin: true,
        scrub: 1,
        start: 'top top',
        end: () => `+=${totalScrollWidth}`,
        invalidateOnRefresh: true,
      }
    });
  }

  // 4. CRAFTSMANSHIP SCROLL REVEALS
  const craftRows = document.querySelectorAll('.craft-step-row');
  craftRows.forEach((row) => {
    const num = row.querySelector('.craft-step-num');
    const content = row.querySelector('.craft-content-pane');
    const img = row.querySelector('.craft-img-frame');

    if (num && content && img) {
      gsap.from([num, content], {
        opacity: 0,
        x: row.classList.contains('reverse') ? 60 : -60,
        duration: 1.2,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: row,
          start: 'top 75%',
          toggleActions: 'play none none reverse',
        }
      });

      gsap.from(img, {
        opacity: 0,
        scale: 0.92,
        duration: 1.4,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: row,
          start: 'top 75%',
          toggleActions: 'play none none reverse',
        }
      });
    }
  });

  // 5. PRODUCT CARDS STAGGERED REVEAL
  const productGrids = document.querySelectorAll('.product-grid');
  productGrids.forEach((grid) => {
    const cards = grid.querySelectorAll('.product-card');
    if (cards.length > 0) {
      gsap.from(cards, {
        opacity: 0,
        y: 40,
        stagger: 0.12,
        duration: 0.9,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: grid,
          start: 'top 80%',
          toggleActions: 'play none none reverse',
        }
      });
    }
  });

  // 6. SECTION HEADERS REVEAL
  const sectionHeaders = document.querySelectorAll('.section-header');
  sectionHeaders.forEach((header) => {
    gsap.from(header.children, {
      opacity: 0,
      y: 30,
      stagger: 0.15,
      duration: 1,
      ease: 'power3.out',
      scrollTrigger: {
        trigger: header,
        start: 'top 85%',
        toggleActions: 'play none none reverse',
      }
    });
  });

  // 7. MAGNETIC BUTTON EFFECT
  const magneticBtns = document.querySelectorAll('.magnetic-btn');
  magneticBtns.forEach((btn) => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      gsap.to(btn, { x: x * 0.3, y: y * 0.3, duration: 0.3, ease: 'power2.out' });
    });

    btn.addEventListener('mouseleave', () => {
      gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.4)' });
    });
  });
});
