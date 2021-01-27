from django.contrib import admin

# Register your models here.

from core.models import Usuario, Linguagem, Perguntas, Alternativas, Ranking


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'senha', 'email')


class LinguagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fundador', 'ano')


class PerguntasAdmin(admin.ModelAdmin):
    list_display = ('linguagem', 'numeracao', 'pontuacao')


class AlternativasAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'letras', 'letraCerta')


class RangingAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'score')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Linguagem, LinguagemAdmin)
admin.site.register(Perguntas, PerguntasAdmin)
admin.site.register(Alternativas, AlternativasAdmin)
admin.site.register(Ranking, RangingAdmin)