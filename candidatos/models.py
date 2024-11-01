from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

telefone_validator = RegexValidator(
    regex=r"^\+?1?\d{9,15}$", message="O telefone deve ter 9 a 15 dígitos."
)


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)


class ExperienciaProfissional(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descricao = models.TextField()
    periodo_inicio = models.DateField()
    periodo_fim = models.DateField()

    def clean(self):
        if (
            self.periodo_inicio
            and self.periodo_fim
            and self.periodo_inicio > self.periodo_fim
        ):
            raise ValidationError("A data de início deve ser anterior à data de fim.")


class FormacaoAcademica(models.Model):
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    periodo_inicio = models.DateField()
    periodo_fim = models.DateField()

    def clean(self):
        if (
            self.periodo_inicio
            and self.periodo_fim
            and self.periodo_inicio > self.periodo_fim
        ):
            raise ValidationError("A data de início deve ser anterior à data de fim.")


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, validators=[telefone_validator])
    cargo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=20)
    skills = models.TextField(blank=True)
    languages = models.TextField(blank=True)
    cover_letter = models.TextField(blank=True)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
    )
    experiencias_profissionais = models.ManyToManyField(
        ExperienciaProfissional, through="CandidatoExperienciaProfissional", blank=True
    )
    formacoes_academicas = models.ManyToManyField(
        FormacaoAcademica, through="CandidatoFormacaoAcademica", blank=True
    )


# Modelos intermediários para relacionamentos ManyToMany


class CandidatoExperienciaProfissional(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    experiencia_profissional = models.ForeignKey(
        ExperienciaProfissional, on_delete=models.CASCADE
    )


class CandidatoFormacaoAcademica(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    formacao_academica = models.ForeignKey(FormacaoAcademica, on_delete=models.CASCADE)
