from django.contrib import admin
from .models import (
    Candidato,
    Endereco,
    Contato,
    ExperienciaProfissional,
    FormacaoAcademica,
    Habilidades,
    Certificacao,
)


# Registrando os modelos no Django Admin
class CandidatoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "sobrenome",
        "cpf",
        "data_nascimento",
        "estado_civil",
    )  # Exibe esses campos na listagem
    search_fields = (
        "nome",
        "sobrenome",
        "cpf",
        "rg",
    )  # Permite buscar pelos campos nome, sobrenome, CPF e RG
    list_filter = (
        "estado_civil",
        "nacionalidade",
    )  # Adiciona filtros para estado civil e nacionalidade
    ordering = ("nome",)  # Ordena pela coluna nome
    fieldsets = (  # Organiza os campos no formulário de edição
        (
            "Informações Pessoais",
            {"fields": ("nome", "sobrenome", "data_nascimento", "cpf", "rg")},
        ),
        (
            "Outras Informações",
            {"fields": ("nacionalidade", "estado_civil", "foto_perfil", "curriculo")},
        ),
    )


admin.site.register(Candidato, CandidatoAdmin)


class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        "candidato",
        "rua",
        "numero",
        "cidade",
        "estado",
        "cep",
    )  # Exibe endereço na listagem
    search_fields = (
        "rua",
        "cidade",
        "estado",
        "cep",
    )  # Busca por rua, cidade, estado, e CEP
    list_filter = ("estado", "cidade")  # Filtro por estado e cidade
    ordering = ("cidade", "estado")  # Ordena por cidade e estado
    fieldsets = (  # Organiza os campos no formulário de edição
        (
            "Endereço",
            {
                "fields": (
                    "rua",
                    "numero",
                    "complemento",
                    "cep",
                    "cidade",
                    "estado",
                    "pais",
                )
            },
        ),
    )


admin.site.register(Endereco, EnderecoAdmin)


class ContatoAdmin(admin.ModelAdmin):
    list_display = (
        "candidato",
        "email",
        "telefone_celular",
        "telefone_fixo",
    )  # Exibe contato na listagem
    search_fields = (
        "email",
        "telefone_celular",
    )  # Permite buscar pelo email e telefone celular
    list_filter = ("email",)  # Filtro pelo campo email
    ordering = ("email",)  # Ordena por email
    fieldsets = (  # Organiza os campos no formulário de edição
        ("Contato", {"fields": ("email", "telefone_celular", "telefone_fixo")}),
    )


admin.site.register(Contato, ContatoAdmin)


class ExperienciaProfissionalAdmin(admin.ModelAdmin):
    list_display = (
        "candidato",
        "cargo",
        "empresa",
        "data_inicio",
        "data_fim",
    )  # Exibe experiência na listagem
    search_fields = ("cargo", "empresa")  # Permite buscar por cargo e empresa
    list_filter = ("empresa", "data_inicio")  # Filtro por empresa e data de início
    ordering = ("data_inicio",)  # Ordena por data de início
    fieldsets = (  # Organiza os campos no formulário de edição
        (
            "Experiência Profissional",
            {
                "fields": (
                    "cargo",
                    "empresa",
                    "data_inicio",
                    "data_fim",
                    "descricao",
                    "responsavel",
                    "contato_responsavel",
                    "habilidades_utilizadas",
                ),
            },
        ),
    )


admin.site.register(ExperienciaProfissional, ExperienciaProfissionalAdmin)


class FormacaoAcademicaAdmin(admin.ModelAdmin):
    list_display = (
        "candidato",
        "instituicao",
        "curso",
        "data_inicio",
        "data_fim",
        "tipo",
    )  # Exibe formação na listagem
    search_fields = ("instituicao", "curso")  # Permite buscar por instituição e curso
    list_filter = ("instituicao", "tipo")  # Filtro por instituição e tipo de formação
    ordering = ("data_inicio",)  # Ordena por data de início
    fieldsets = (  # Organiza os campos no formulário de edição
        (
            "Formação Acadêmica",
            {
                "fields": (
                    "instituicao",
                    "curso",
                    "data_inicio",
                    "data_fim",
                    "tipo",
                    "nota_final",
                    "descricao",
                ),
            },
        ),
    )


admin.site.register(FormacaoAcademica, FormacaoAcademicaAdmin)


class HabilidadesAdmin(admin.ModelAdmin):
    list_display = (
        "candidato",
        "nome",
        "nivel",
    )  # Exibe habilidade e nível na listagem
    search_fields = ("nome",)  # Permite buscar pelo nome da habilidade
    list_filter = ("nivel",)  # Filtro por nível de habilidade
    ordering = ("nome",)  # Ordena pelo nome da habilidade
    fieldsets = (  # Organiza os campos no formulário de edição
        (
            "Habilidade",
            {
                "fields": ("nome", "nivel"),
            },
        ),
    )


admin.site.register(Habilidades, HabilidadesAdmin)


class CertificacaoAdmin(admin.ModelAdmin):
    list_display = (
        "candidato",
        "nome_certificacao",
        "instituicao_emissora",
        "data_emissao",
        "data_validade",
    )  # Exibe certificação na listagem
    search_fields = (
        "nome_certificacao",
        "instituicao_emissora",
    )  # Busca por nome da certificação e instituição
    list_filter = (
        "instituicao_emissora",
        "data_emissao",
    )  # Filtro por instituição e data de emissão
    ordering = ("data_emissao",)  # Ordena por data de emissão
    fieldsets = (  # Organiza os campos no formulário de edição
        (
            "Certificação",
            {
                "fields": (
                    "nome_certificacao",
                    "instituicao_emissora",
                    "data_emissao",
                    "data_validade",
                ),
            },
        ),
    )


admin.site.register(Certificacao, CertificacaoAdmin)
