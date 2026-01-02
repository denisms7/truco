from score.models import Partida
import logging


logger = logging.getLogger(__name__)


def save_score(vencedor, placar_a, placar_b):

    try:
        # Validações básicas
        if not vencedor:
            logger.error("Tentativa de salvar partida sem vencedor definido")
            return None

        if placar_a is None or placar_b is None:
            logger.error(f"Tentativa de salvar partida com placar inválido: A={placar_a}, B={placar_b}")
            return None

        if placar_a < 0 or placar_b < 0:
            logger.error(f"Tentativa de salvar partida com placar negativo: A={placar_a}, B={placar_b}")
            return None

        # Cria a partida
        partida = Partida.objects.create(
            vencedor=vencedor,
            placar_final_a=placar_a,
            placar_final_b=placar_b,
        )

        logger.info(f"Partida salva com sucesso: ID={partida.id}, Vencedor={vencedor}")
        return partida

    except Exception as e:
        logger.exception(f"Erro ao salvar partida: vencedor={vencedor}, placar_a={placar_a}, placar_b={placar_b}. Detalhes: {e}")
