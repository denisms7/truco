function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {
            cookie = cookie.trim();

            if (cookie.startsWith(`${name}=`)) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function atualizarPlacar(data) {
    document.getElementById("score-A").innerText = data.score_a;
    document.getElementById("score-B").innerText = data.score_b;
    document.getElementById("victory-A").innerText = data.victory_a;
    document.getElementById("victory-B").innerText = data.victory_b;

    if (data.winner) {
        destacarVitoria(data.winner);
        soltarConfete();
    }
}

function carregarStatus() {
    fetch(window.STATUS_PLACAR_URL)
        .then((r) => r.json())
        .then((data) => atualizarPlacar(data))
        .catch((e) => console.error("Erro ao carregar status:", e));
}

function alterarScore(time, op) {
    const params = new URLSearchParams({ time, op });

    fetch(window.ALTERAR_PONTUACAO_URL, {
        method: "POST",
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        body: params,
    })
        .then((r) => r.json())
        .then((data) => {
            carregarStatus();

            if (data.winner) {
                destacarVitoria(data.winner);
                soltarConfete();
            }
        })
        .catch((e) => console.error("Erro ao alterar score:", e));
}

function resetarPlacar() {
    fetch(window.RESETAR_PLACAR_URL, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        },
    })
        .then((r) => {
            if (!r.ok) {
                throw new Error(`Erro HTTP ${r.status}`);
            }
            return r.json();
        })
        .then((data) => atualizarPlacar(data))
        .catch((e) => console.error("Erro ao resetar placar:", e));
}

document.addEventListener("DOMContentLoaded", () => {
    carregarStatus();

    document.getElementById("btn-reset").addEventListener("click", resetarPlacar);
});
