from score.models import Partida


def salvar_partida(vencedor, placar_a, placar_b):
    """
    Salva uma partida no momento da vitória.
    Esta função NÃO altera sessão nem regras de jogo.
    """
    return Partida.objects.create(
        vencedor=vencedor,
        placar_final_a=placar_a,
        placar_final_b=placar_b,
    )
