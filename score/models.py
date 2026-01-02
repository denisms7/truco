from django.db import models


class Partida(models.Model):
    criada_em = models.DateTimeField(auto_now_add=True)
    vencedor = models.CharField(
        max_length=1,
        choices=[("A", "Time A"), ("B", "Time B")],
    )
    placar_final_a = models.PositiveSmallIntegerField()
    placar_final_b = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Partida {self.id} - Vencedor {self.vencedor}"
