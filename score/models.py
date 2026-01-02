from django.db import models
from django.utils.translation import gettext_lazy as _


class Partida(models.Model):
    criada_em = models.DateTimeField(auto_now_add=True)
    vencedor = models.CharField(
        max_length=1,
        choices=[("A", _("Time A")), ("B", _("Time B"))],
    )
    placar_final_a = models.PositiveSmallIntegerField()
    placar_final_b = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{_('Partida')} {self.id} - {_('Vencedor')} {self.vencedor}"
