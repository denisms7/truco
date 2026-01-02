import logging
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from score.services import save_score


logger = logging.getLogger(__name__)


class HomeTemplateView(TemplateView):
    template_name = "score/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        session = self.request.session
        session.setdefault("score_a", 0)
        session.setdefault("score_b", 0)
        session.setdefault("victory_a", 0)
        session.setdefault("victory_b", 0)

        context["score_a"] = session["score_a"]
        context["score_b"] = session["score_b"]
        context["victory_a"] = session["victory_a"]
        context["victory_b"] = session["victory_b"]

        return context


class StatusView(View):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "score_a": request.session.get("score_a", 0),
                "score_b": request.session.get("score_b", 0),
                "victory_a": request.session.get("victory_a", 0),
                "victory_b": request.session.get("victory_b", 0),
            }
        )


@method_decorator(require_POST, name="dispatch")
class ModifyView(View):
    MAX_SCORE = 12

    def post(self, request, *args, **kwargs):
        time = request.POST.get("time")
        operacao = request.POST.get("op")

        score_a = request.session.get("score_a", 0)
        score_b = request.session.get("score_b", 0)
        victory_a = request.session.get("victory_a", 0)
        victory_b = request.session.get("victory_b", 0)

        winner = None

        if operacao == "inc":
            if time == "A" and score_a < self.MAX_SCORE:
                score_a += 1
                if score_a == self.MAX_SCORE:
                    victory_a += 1
                    winner = "A"

            elif time == "B" and score_b < self.MAX_SCORE:
                score_b += 1
                if score_b == self.MAX_SCORE:
                    victory_b += 1
                    winner = "B"

        elif operacao == "dec":
            if time == "A" and score_a > 0:
                score_a -= 1
            elif time == "B" and score_b > 0:
                score_b -= 1

        if winner:
            partida = save_score(winner, score_a, score_b)
            if partida:
                logger.info(f"Partida salva: {partida.id}")
                score_a = 0
                score_b = 0
            else:
                logger.warning("Falha ao salvar partida, mas o jogo continua")
                # Mesmo com erro ao salvar, resetamos o placar para continuar jogando
                score_a = 0
                score_b = 0

        request.session["score_a"] = score_a
        request.session["score_b"] = score_b
        request.session["victory_a"] = victory_a
        request.session["victory_b"] = victory_b
        request.session.modified = True

        return JsonResponse({"winner": winner})


@method_decorator(require_POST, name="dispatch")
class ResetView(View):
    def post(self, request, *args, **kwargs):
        request.session["score_a"] = 0
        request.session["score_b"] = 0
        request.session["victory_a"] = 0
        request.session["victory_b"] = 0
        request.session.modified = True

        return JsonResponse(
            {
                "score_a": 0,
                "score_b": 0,
                "victory_a": 0,
                "victory_b": 0,
            }
        )
