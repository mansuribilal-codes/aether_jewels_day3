/**
 * AETHER JEWELS – Synthesized Cosmic Soundscape & Tactile Chimes
 * Built with Web Audio API for 100% reliable offline / browser execution.
 */

const CelestialSound = (function () {
  let audioCtx = null;
  let isMuted = true;
  let masterGain = null;
  let droneOscillators = [];

  function initAudio() {
    if (!audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioContext();
      masterGain = audioCtx.createGain();
      masterGain.gain.setValueAtTime(0.25, audioCtx.currentTime);
      masterGain.connect(audioCtx.destination);
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  }

  function startDrone() {
    if (!audioCtx || isMuted) return;
    stopDrone();

    // Cosmic Celestial Chord: F# Minor / Cosmic 432Hz ambient tuning
    const freqs = [92.5, 138.59, 185.0, 277.18]; // F#2, C#3, F#3, C#4

    freqs.forEach((f) => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      const filter = audioCtx.createBiquadFilter();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(f, audioCtx.currentTime);

      // Low pass filter for warm cosmic pad sound
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(400, audioCtx.currentTime);

      // Soft envelope
      gain.gain.setValueAtTime(0.001, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.05, audioCtx.currentTime + 2.5);

      osc.connect(filter);
      filter.connect(gain);
      gain.connect(masterGain);

      osc.start();
      droneOscillators.push({ osc, gain });
    });
  }

  function stopDrone() {
    if (droneOscillators.length > 0 && audioCtx) {
      droneOscillators.forEach(({ osc, gain }) => {
        try {
          gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 1.2);
          setTimeout(() => {
            try { osc.stop(); } catch (e) {}
          }, 1300);
        } catch (e) {}
      });
      droneOscillators = [];
    }
  }

  function playCrystalChime(freq = 1174.66) { // D6 crystal tone
    if (isMuted) return;
    try {
      initAudio();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.8);

      osc.connect(gain);
      gain.connect(masterGain);

      osc.start();
      osc.stop(audioCtx.currentTime + 0.8);
    } catch (e) {}
  }

  function updateUI() {
    const soundBtns = document.querySelectorAll('.sound-toggle-btn');
    soundBtns.forEach(btn => {
      if (!isMuted) {
        btn.classList.add('active-sound');
        btn.setAttribute('title', 'Mute Celestial Soundscape');
        btn.innerHTML = '<i class="ri-volume-up-line"></i>';
      } else {
        btn.classList.remove('active-sound');
        btn.setAttribute('title', 'Enable Celestial Soundscape');
        btn.innerHTML = '<i class="ri-volume-mute-line"></i>';
      }
    });
  }

  function toggleSound() {
    initAudio();
    isMuted = !isMuted;

    if (!isMuted) {
      localStorage.setItem('aether_soundscape', 'active');
      startDrone();
      playCrystalChime(880);
      if (window.showToast) window.showToast('Celestial Ambient Soundscape Activated.', 'info');
    } else {
      localStorage.setItem('aether_soundscape', 'muted');
      stopDrone();
      if (window.showToast) window.showToast('Soundscape Muted.', 'info');
    }

    updateUI();
    return !isMuted;
  }

  // Bind interactive tactile sound to luxury buttons
  document.addEventListener('DOMContentLoaded', () => {
    // Check saved state (default is muted to comply with browser autoplay policy)
    const savedState = localStorage.getItem('aether_soundscape');
    if (savedState === 'active') {
      // Show prompt or ready state
      isMuted = true;
    }
    updateUI();

    // Direct click handler on sound toggle buttons
    document.addEventListener('click', (e) => {
      const toggleBtn = e.target.closest('.sound-toggle-btn');
      if (toggleBtn) {
        e.preventDefault();
        e.stopPropagation();
        toggleSound();
        return;
      }

      // Tactile chime on interactive cards and buttons when sound is active
      const btn = e.target.closest('.btn, .showcase-card, .product-card, .lounge-card-option, .config-option-card');
      if (btn && !isMuted) {
        playCrystalChime(1318.51); // E6 sparkle chime
      }
    });
  });

  return {
    toggle: toggleSound,
    chime: playCrystalChime,
    isMuted: () => isMuted,
  };
})();
