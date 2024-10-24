# serializers.py
from rest_framework import serializers
from .models import (
    Candidato,
    Endereco,
    Contato,
    ExperienciaProfissional,
    FormacaoAcademica,
    Habilidades,
    Certificacao,
)


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = "__all__"  # Inclui todos os campos do modelo


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = "__all__"


class ExperienciaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaProfissional
        fields = "__all__"


class FormacaoAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormacaoAcademica
        fields = "__all__"


class HabilidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidades
        fields = "__all__"


class CertificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificacao
        fields = "__all__"
