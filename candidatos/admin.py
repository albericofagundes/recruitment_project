from django.contrib import admin
from .models import (
    Endereco,
    ExperienciaProfissional,
    FormacaoAcademica,
    Candidato,
    CandidatoExperienciaProfissional,
    CandidatoFormacaoAcademica,
)


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("rua", "numero", "cidade", "estado", "cep")
    search_fields = ("rua", "numero", "cidade", "estado", "cep")


class ExperienciaProfissionalAdmin(admin.ModelAdmin):
    list_display = ("cargo", "empresa", "periodo_inicio", "periodo_fim")
    search_fields = ("cargo", "empresa")
    list_filter = ("periodo_inicio", "periodo_fim")


class FormacaoAcademicaAdmin(admin.ModelAdmin):
    list_display = ("instituicao", "curso", "periodo_inicio", "periodo_fim")
    search_fields = ("instituicao", "curso")
    list_filter = ("periodo_inicio", "periodo_fim")


class CandidatoExperienciaProfissionalInline(admin.TabularInline):
    model = CandidatoExperienciaProfissional
    extra = 1
    verbose_name = "Experiência Profissional"
    verbose_name_plural = "Experiências Profissionais"


class CandidatoFormacaoAcademicaInline(admin.TabularInline):
    model = CandidatoFormacaoAcademica
    extra = 1
    verbose_name = "Formação Acadêmica"
    verbose_name_plural = "Formações Acadêmicas"


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "cargo", "data_nascimento")
    search_fields = ("nome", "email", "telefone", "cargo")
    list_filter = ("cargo", "data_nascimento", "estado_civil")
    ordering = ("-data_nascimento",)
    fieldsets = (
        (
            "Informações Pessoais",
            {
                "fields": (
                    "nome",
                    "email",
                    "telefone",
                    "cargo",
                    "data_nascimento",
                    "nacionalidade",
                    "estado_civil",
                )
            },
        ),
        ("Outras Informações", {"fields": ("skills", "languages", "cover_letter")}),
        ("Endereço", {"fields": ("endereco",)}),
    )
    inlines = [CandidatoExperienciaProfissionalInline, CandidatoFormacaoAcademicaInline]


admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(ExperienciaProfissional, ExperienciaProfissionalAdmin)
admin.site.register(FormacaoAcademica, FormacaoAcademicaAdmin)
admin.site.register(Candidato, CandidatoAdmin)
