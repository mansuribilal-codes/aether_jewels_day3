/**
 * AETHER JEWELS – Main Luxury UI Controller
 */

// Global Toast System
window.showToast = function (message, type = 'gold') {
  let container = document.getElementById('luxury-toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'luxury-toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'luxury-toast';

  let icon = 'ri-sparkling-fill';
  if (type === 'error') icon = 'ri-error-warning-line';
  else if (type === 'info') icon = 'ri-information-line';

  toast.innerHTML = `
    <i class="${icon}"></i>
    <div style="flex: 1;">
      <p style="margin: 0; line-height: 1.4;">${message}</p>
    </div>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    toast.style.transition = 'all 0.4s ease';
    setTimeout(() => toast.remove(), 400);
  }, 4500);
};

document.addEventListener('DOMContentLoaded', () => {
  // 1. NAVBAR SCROLL WATCHER
  const navbar = document.querySelector('.luxury-nav');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 30) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // 2. MOBILE DRAWER & ANIMATED HAMBURGER TOGGLE
  const mobileToggle = document.getElementById('mobile-nav-toggle') || document.querySelector('.mobile-nav-toggle');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const mobileBackdrop = document.getElementById('mobile-nav-backdrop');
  const mobileClose = document.getElementById('mobile-drawer-close') || document.querySelector('.mobile-drawer-close');

  function openMobileMenu() {
    if (mobileDrawer) mobileDrawer.classList.add('open');
    if (mobileBackdrop) mobileBackdrop.classList.add('open');
    if (mobileToggle) {
      mobileToggle.classList.add('active');
      mobileToggle.setAttribute('aria-expanded', 'true');
    }
    document.body.style.overflow = 'hidden';
  }

  function closeMobileMenu() {
    if (mobileDrawer) mobileDrawer.classList.remove('open');
    if (mobileBackdrop) mobileBackdrop.classList.remove('open');
    if (mobileToggle) {
      mobileToggle.classList.remove('active');
      mobileToggle.setAttribute('aria-expanded', 'false');
    }
    document.body.style.overflow = '';
  }

  function toggleMobileMenu() {
    if (mobileDrawer && mobileDrawer.classList.contains('open')) {
      closeMobileMenu();
    } else {
      openMobileMenu();
    }
  }

  if (mobileToggle) mobileToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleMobileMenu();
  });
  if (mobileClose) mobileClose.addEventListener('click', closeMobileMenu);
  if (mobileBackdrop) mobileBackdrop.addEventListener('click', closeMobileMenu);

  // Auto-close on mobile menu link click
  document.querySelectorAll('.mobile-nav-links a').forEach(link => {
    link.addEventListener('click', closeMobileMenu);
  });

  // Close on Escape key press
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileDrawer && mobileDrawer.classList.contains('open')) {
      closeMobileMenu();
    }
  });

  // 3. CURRENCY MODAL TOGGLE
  const currencyBtns = document.querySelectorAll('.currency-trigger-btn');
  const currencyModal = document.getElementById('currency-modal');
  if (currencyBtns && currencyModal) {
    currencyBtns.forEach(b => {
      b.addEventListener('click', () => {
        closeMobileMenu();
        currencyModal.classList.add('open');
      });
    });
  }

  // 4. GENERIC MODAL CLOSE
  document.querySelectorAll('.modal-close-btn, .modal-backdrop, .modal-close-btn-action').forEach(el => {
    el.addEventListener('click', (e) => {
      if (e.target === el || e.target.closest('.modal-close-btn') || e.target.closest('.modal-close-btn-action')) {
        const modal = el.closest('.modal-backdrop');
        if (modal) modal.classList.remove('open');
      }
    });
  });

  // Prevent closing when clicking inside modal window
  document.querySelectorAll('.modal-window').forEach(win => {
    win.addEventListener('click', (e) => e.stopPropagation());
  });

  // 5. QUICK VIEW MODAL DYNAMICS
  const quickviewModal = document.getElementById('quickview-modal');
  document.addEventListener('click', async (e) => {
    const qvBtn = e.target.closest('.card-quickview-btn');
    if (qvBtn && quickviewModal) {
      e.preventDefault();
      const productId = qvBtn.dataset.productId;
      if (!productId) return;

      quickviewModal.classList.add('open');
      const container = document.getElementById('quickview-content');
      if (container) {
        container.innerHTML = `
          <div style="padding: 4rem; text-align: center;">
            <i class="ri-loader-4-line ri-spin" style="font-size: 2.5rem; color: var(--gold-primary);"></i>
            <p style="margin-top: 1rem; color: var(--gold-champagne);">Accessing Sovereign Vault Registry...</p>
          </div>
        `;

        try {
          const res = await fetch(`/api/products/${productId}/quickview/`);
          const data = await res.json();
          if (data.success) {
            const p = data.product;
            container.innerHTML = `
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; padding: 2.5rem;">
                <div style="background: #0D0E14; border-radius: var(--radius-sm); overflow: hidden; display: flex; align-items: center; justify-content: center;">
                  <img src="${p.image_primary}" alt="${p.title}" style="width: 100%; height: 380px; object-fit: cover;">
                </div>
                <div style="display: flex; flex-direction: column; justify-content: space-between;">
                  <div>
                    <span class="badge-gold" style="margin-bottom: 0.75rem;">${p.certification}</span>
                    <h2 style="font-size: 1.6rem; margin-bottom: 0.5rem;">${p.title}</h2>
                    <p style="font-family: var(--font-serif-editorial); font-style: italic; color: var(--gold-light); font-size: 1.1rem; margin-bottom: 1rem;">${p.subtitle}</p>
                    <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 1.25rem;">${p.description}</p>
                    <div style="background: var(--bg-surface-2); padding: 1rem; border-radius: var(--radius-sm); border: 1px solid rgba(212,175,55,0.15); margin-bottom: 1.5rem;">
                      <div style="font-size: 0.75rem; color: var(--text-muted);">PRIMARY GEMSTONE: <strong style="color: var(--ivory-soft);">${p.primary_gemstone}</strong></div>
                      <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">PRECIOUS METAL: <strong style="color: var(--ivory-soft);">${p.metal_description}</strong></div>
                      <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">CARAT WEIGHT: <strong style="color: var(--ivory-soft);">${p.carat_weight} ct</strong></div>
                    </div>
                  </div>
                  <div>
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem;">
                      <span style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--text-muted);">Sovereign Valuation</span>
                      <span class="product-price-val" data-price-inr="${p.price_inr}" style="font-size: 1.4rem;">${p.formatted_price}</span>
                    </div>
                    <div style="display: flex; gap: 1rem;">
                      <a href="${p.url}" class="btn btn-gold" style="flex: 1;">Complete Dossier</a>
                      <a href="/book-consultation/" class="btn btn-outline-gold" style="flex: 1;">Reserve Viewing</a>
                    </div>
                  </div>
                </div>
              </div>
            `;
            if (window.CurrencyConverter) window.CurrencyConverter.refresh();
          }
        } catch (err) {
          container.innerHTML = `<p style="padding: 2rem; color: #ff6b6b;">Failed to load jewel specifications.</p>`;
        }
      }
    }
  });

  // 6. VIP CONSULTATION BOOKING FORM SUBMIT
  const consultationForm = document.getElementById('consultation-booking-form');
  if (consultationForm) {
    document.querySelectorAll('.lounge-card-option').forEach(card => {
      card.addEventListener('click', function () {
        document.querySelectorAll('.lounge-card-option').forEach(c => c.classList.remove('selected'));
        this.classList.add('selected');
        const loungeInput = consultationForm.querySelector('#city-lounge-input');
        if (loungeInput) loungeInput.value = this.dataset.lounge;
      });
    });

    consultationForm.addEventListener('submit', async function (e) {
      e.preventDefault();
      const form = this;
      const submitBtn = form.querySelector('button[type="submit"]');

      const fullName = form.querySelector('#client-fullname')?.value.trim();
      const email = form.querySelector('#client-booking-email')?.value.trim();
      const phone = form.querySelector('#client-booking-phone')?.value.trim();
      const cityLounge = form.querySelector('#city-lounge-input')?.value || 'The Bandra Celestial Suite, Mumbai';
      const preferredDate = form.querySelector('#booking-date')?.value;
      const preferredTime = form.querySelector('#booking-time')?.value || '11:30 AM';
      const jewelleryInterest = form.querySelector('#jewellery-interest')?.value || 'Celestial High Jewellery';
      const hospitality = form.querySelector('#hospitality-preference')?.value || 'Dom Pérignon Vintage Champagne';
      const notes = form.querySelector('#booking-notes')?.value.trim() || '';

      if (!fullName || !email || !phone || !preferredDate) {
        window.showToast('Please complete all mandatory appointment fields.', 'error');
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="ri-loader-4-line ri-spin"></i> Securing Flagship Salon...';
      }

      try {
        const response = await fetch('/api/consultation/book/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') || '',
          },
          body: JSON.stringify({
            full_name: fullName,
            email: email,
            phone: phone,
            city_lounge: cityLounge,
            preferred_date: preferredDate,
            preferred_time: preferredTime,
            jewellery_interest: jewelleryInterest,
            hospitality_preference: hospitality,
            notes: notes,
          })
        });

        const data = await response.json();

        if (data.success) {
          window.showToast(data.message, 'success');
          form.reset();

          const confirmModal = document.getElementById('consultation-confirmed-modal');
          if (confirmModal) {
            const bookingIdElem = document.getElementById('confirmed-booking-id');
            if (bookingIdElem) bookingIdElem.textContent = data.booking_id;
            confirmModal.classList.add('open');
          }
        } else {
          window.showToast(data.error || 'Unable to process reservation.', 'error');
        }
      } catch (err) {
        window.showToast('Connection error. Please call Concierge directly at +91 22 8920 4400.', 'error');
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<i class="ri-calendar-check-line"></i> Confirm Private Viewing';
        }
      }
    });
  }

  // 7. CINEMATIC VIDEO CONTROLS
  const video = document.getElementById('atelier-cinema-video');
  const playBtn = document.getElementById('cinema-play-btn');

  if (video && playBtn) {
    playBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();

      if (video.paused) {
        video.muted = true; // Required for reliable autoplay in modern browsers
        const playPromise = video.play();
        if (playPromise !== undefined) {
          playPromise.then(() => {
            playBtn.innerHTML = '<i class="ri-pause-line"></i>';
            playBtn.style.opacity = '0.35';
          }).catch(error => {
            console.log('Autoplay handled:', error);
          });
        }
      } else {
        video.pause();
        playBtn.innerHTML = '<i class="ri-play-fill"></i>';
        playBtn.style.opacity = '1';
      }
    });

    video.addEventListener('play', () => {
      playBtn.innerHTML = '<i class="ri-pause-line"></i>';
    });

    video.addEventListener('pause', () => {
      playBtn.innerHTML = '<i class="ri-play-fill"></i>';
      playBtn.style.opacity = '1';
    });

    video.addEventListener('ended', () => {
      playBtn.innerHTML = '<i class="ri-play-fill"></i>';
      playBtn.style.opacity = '1';
    });

    const cinemaFrame = document.querySelector('.cinema-frame');
    if (cinemaFrame) {
      cinemaFrame.addEventListener('mouseenter', () => {
        playBtn.style.opacity = '1';
      });
      cinemaFrame.addEventListener('mouseleave', () => {
        if (!video.paused) playBtn.style.opacity = '0.25';
      });
    }
  }

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
