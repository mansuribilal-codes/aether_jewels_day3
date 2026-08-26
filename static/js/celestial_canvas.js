/**
 * AETHER JEWELS – Dynamic Celestial Starfield & Nebula Particle Canvas
 */

(function () {
  const canvas = document.getElementById('celestial-bg-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width, height;
  let stars = [];
  let meteors = [];
  let mouse = { x: null, y: null, targetX: null, targetY: null };

  const STAR_COUNT = 140;
  const GOLD_PALETTE = ['#FFFFFF', '#F3E5AB', '#D4AF37', '#E0A99A', '#997929'];

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    initStars();
  }

  function initStars() {
    stars = [];
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        baseX: Math.random() * width,
        baseY: Math.random() * height,
        size: Math.random() * 1.8 + 0.4,
        color: GOLD_PALETTE[Math.floor(Math.random() * GOLD_PALETTE.length)],
        alpha: Math.random() * 0.7 + 0.2,
        twinkleSpeed: (Math.random() * 0.02 + 0.005) * (Math.random() > 0.5 ? 1 : -1),
        speedX: (Math.random() - 0.5) * 0.15,
        speedY: (Math.random() - 0.5) * 0.15,
      });
    }
  }

  function spawnMeteor() {
    if (meteors.length < 2 && Math.random() < 0.008) {
      meteors.push({
        x: Math.random() * width,
        y: Math.random() * (height * 0.4),
        length: Math.random() * 80 + 50,
        speed: Math.random() * 8 + 6,
        angle: Math.PI / 4 + (Math.random() - 0.5) * 0.2,
        alpha: 1,
        life: 0,
      });
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    // Mouse lerp
    if (mouse.targetX !== null) {
      mouse.x += (mouse.targetX - mouse.x) * 0.05;
      mouse.y += (mouse.targetY - mouse.y) * 0.05;
    }

    // Draw Stars
    for (let i = 0; i < stars.length; i++) {
      const star = stars[i];

      // Twinkle
      star.alpha += star.twinkleSpeed;
      if (star.alpha > 0.95 || star.alpha < 0.15) {
        star.twinkleSpeed = -star.twinkleSpeed;
      }

      // Gentle Drift
      star.x += star.speedX;
      star.y += star.speedY;
      if (star.x < 0) star.x = width;
      if (star.x > width) star.x = 0;
      if (star.y < 0) star.y = height;
      if (star.y > height) star.y = 0;

      // Mouse Parallax Gravity
      let dx = star.x - (mouse.x || width / 2);
      let dy = star.y - (mouse.y || height / 2);
      let dist = Math.sqrt(dx * dx + dy * dy);
      let offsetX = 0;
      let offsetY = 0;

      if (dist < 180) {
        let force = (180 - dist) / 180;
        offsetX = (dx / dist) * force * 15;
        offsetY = (dy / dist) * force * 15;
      }

      ctx.save();
      ctx.globalAlpha = star.alpha;
      ctx.fillStyle = star.color;
      ctx.beginPath();
      ctx.arc(star.x + offsetX, star.y + offsetY, star.size, 0, Math.PI * 2);
      ctx.fill();

      // Subtle glow for larger stars
      if (star.size > 1.4) {
        ctx.shadowBlur = 8;
        ctx.shadowColor = star.color;
        ctx.fill();
      }
      ctx.restore();
    }

    // Draw Meteors (Shooting Stars)
    spawnMeteor();
    for (let i = meteors.length - 1; i >= 0; i--) {
      const m = meteors[i];
      m.x += Math.cos(m.angle) * m.speed;
      m.y += Math.sin(m.angle) * m.speed;
      m.alpha -= 0.015;

      if (m.alpha <= 0 || m.x > width || m.y > height) {
        meteors.splice(i, 1);
        continue;
      }

      ctx.save();
      ctx.globalAlpha = m.alpha;
      let grad = ctx.createLinearGradient(
        m.x, m.y,
        m.x - Math.cos(m.angle) * m.length,
        m.y - Math.sin(m.angle) * m.length
      );
      grad.addColorStop(0, '#FFFFFF');
      grad.addColorStop(0.3, '#D4AF37');
      grad.addColorStop(1, 'transparent');

      ctx.strokeStyle = grad;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(m.x, m.y);
      ctx.lineTo(
        m.x - Math.cos(m.angle) * m.length,
        m.y - Math.sin(m.angle) * m.length
      );
      ctx.stroke();
      ctx.restore();
    }

    requestAnimationFrame(animate);
  }

  window.addEventListener('resize', resize);
  window.addEventListener('mousemove', (e) => {
    mouse.targetX = e.clientX;
    mouse.targetY = e.clientY;
  });

  resize();
  animate();
})();
