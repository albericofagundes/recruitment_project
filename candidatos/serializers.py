from rest_framework import serializers
from .models import Endereco, ExperienciaProfissional, FormacaoAcademica, Candidato


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class ExperienciaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaProfissional
        fields = "__all__"


class FormacaoAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormacaoAcademica
        fields = "__all__"


class CandidatoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(required=False)
    experiencias_profissionais = ExperienciaProfissionalSerializer(
        many=True, required=False
    )
    formacoes_academicas = FormacaoAcademicaSerializer(many=True, required=False)

    class Meta:
        model = Candidato
        fields = "__all__"

    def create(self, validated_data):
        endereco_data = validated_data.pop("endereco", None)
        experiencias_data = validated_data.pop("experiencias_profissionais", [])
        formacoes_data = validated_data.pop("formacoes_academicas", [])

        candidato = Candidato.objects.create(**validated_data)

        if endereco_data:
            endereco = Endereco.objects.create(**endereco_data)
            candidato.endereco = endereco
            candidato.save()

        for experiencia_data in experiencias_data:
            experiencia = ExperienciaProfissional.objects.create(**experiencia_data)
            candidato.experiencias_profissionais.add(experiencia)

        for formacao_data in formacoes_data:
            formacao = FormacaoAcademica.objects.create(**formacao_data)
            candidato.formacoes_academicas.add(formacao)

        return candidato


class CandidatoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ["nome", "email", "cargo", "telefone"]
