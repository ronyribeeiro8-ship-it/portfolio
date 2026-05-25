(function () {
  const cv = document.getElementById('mx');
  const cx = cv.getContext('2d');
  const CH = '01アイウエオカキクケコサシスセソタナニヌネノABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789∑∆≈∞';
  const FS = 14;
  let cols, drops;

  function resize() {
    cv.width  = window.innerWidth;
    cv.height = window.innerHeight;
    cols  = Math.floor(cv.width / FS);
    drops = Array.from({ length: cols }, () => Math.random() * -100);
  }

  function draw() {
    cx.fillStyle = 'rgba(5,10,14,0.05)';
    cx.fillRect(0, 0, cv.width, cv.height);
    for (let i = 0; i < drops.length; i++) {
      cx.fillStyle = Math.random() > .95 ? '#ffffff' : '#00ff88';
      cx.font = FS + 'px "Share Tech Mono",monospace';
      cx.fillText(CH[Math.floor(Math.random() * CH.length)], i * FS, drops[i] * FS);
      if (drops[i] * FS > cv.height && Math.random() > .975) drops[i] = 0;
      drops[i] += 0.5;
    }
  }

  window.addEventListener('resize', resize);
  resize();
  setInterval(draw, 40);
})();
