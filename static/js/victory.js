function destacarVitoria(time) {
    const scoreEl = document.getElementById(`score-${time}`);
    if (!scoreEl) return;

    scoreEl.classList.add("winner");
    setTimeout(() => scoreEl.classList.remove("winner"), 2000);
}

function soltarConfete(qtd = 200) {
    const confetti = document.getElementById("confetti");
    if (!confetti) return;

    confetti.innerHTML = "";

    const colors = ["#ff0", "#0f0", "#00f", "#f00", "#ff00ff", "#00ffff", "#ffa500", "#ff1493", "#00ff00", "#7fff00", "#FFD700", "#FF69B4"];

    for (let i = 0; i < qtd; i += 1) {
        const span = document.createElement("span");

        const direction = Math.floor(Math.random() * 4);
        const drift = (Math.random() - 0.5) * 60;

        if (direction === 0) {
            span.style.top = "-20px";
            span.style.left = `${Math.random() * 100}vw`;
            span.dataset.direction = "top";
            span.style.setProperty('--drift', `${drift}vw`);
        } else if (direction === 1) {
            span.style.bottom = "-20px";
            span.style.left = `${Math.random() * 100}vw`;
            span.dataset.direction = "bottom";
            span.style.setProperty('--drift', `${drift}vw`);
        } else if (direction === 2) {
            span.style.left = "-20px";
            span.style.top = `${Math.random() * 100}vh`;
            span.dataset.direction = "left";
            span.style.setProperty('--drift', `${drift}vh`);
        } else {
            span.style.right = "-20px";
            span.style.top = `${Math.random() * 100}vh`;
            span.dataset.direction = "right";
            span.style.setProperty('--drift', `${drift}vh`);
        }

        span.style.backgroundColor =
            colors[Math.floor(Math.random() * colors.length)];
        span.style.animationDuration =
            `${1.2 + Math.random() * 1.8}s`;
        span.style.animationDelay = `${Math.random() * 0.4}s`;

        const size = 8 + Math.random() * 8;
        span.style.width = `${size}px`;
        span.style.height = `${size * 1.4}px`;

        confetti.appendChild(span);
    }

    setTimeout(() => {
        confetti.innerHTML = "";
    }, 4500);
}
