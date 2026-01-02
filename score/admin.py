from django.contrib import admin
from django.utils.html import format_html

from .models import Partida


@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = (
        "resultado",
        "vencedor_formatado",
        "placar",
        "criada_em",
    )

    list_filter = (
        "vencedor",
        "criada_em",
    )

    date_hierarchy = "criada_em"

    ordering = ("-criada_em",)

    list_per_page = 25

    search_fields = (
        "vencedor",
    )

    readonly_fields = (
        "vencedor",
        "placar_final_a",
        "placar_final_b",
        "criada_em",
    )

    fieldsets = (
        (
            "Resultado da Partida",
            {
                "fields": (
                    "vencedor",
                    ("placar_final_a", "placar_final_b"),
                )
            },
        ),
        (
            "Informações",
            {
                "fields": ("criada_em",),
            },
        ),
    )

    # ==========================
    # Métodos de exibição
    # ==========================

    @admin.display(description="Placar")
    def placar(self, obj):
        return f"{obj.placar_final_a} x {obj.placar_final_b}"

    @admin.display(description="Resultado")
    def resultado(self, obj):
        return "Vitória"

    @admin.display(description="Vencedor")
    def vencedor_formatado(self, obj):
        cor = "#198754" if obj.vencedor == "A" else "#0d6efd"
        return format_html(
            '<strong style="color:{};">Time {}</strong>',
            cor,
            obj.vencedor,
        )
