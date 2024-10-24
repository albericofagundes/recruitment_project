# views.py
from rest_framework import viewsets
from .models import (
    Candidato,
    Endereco,
    Contato,
    ExperienciaProfissional,
    FormacaoAcademica,
    Habilidades,
    Certificacao,
)
from .serializers import (
    CandidatoSerializer,
    EnderecoSerializer,
    ContatoSerializer,
    ExperienciaProfissionalSerializer,
    FormacaoAcademicaSerializer,
    HabilidadesSerializer,
    CertificacaoSerializer,
)


class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ExperienciaProfissionalViewSet(viewsets.ModelViewSet):
    queryset = ExperienciaProfissional.objects.all()
    serializer_class = ExperienciaProfissionalSerializer


class FormacaoAcademicaViewSet(viewsets.ModelViewSet):
    queryset = FormacaoAcademica.objects.all()
    serializer_class = FormacaoAcademicaSerializer


class HabilidadesViewSet(viewsets.ModelViewSet):
    queryset = Habilidades.objects.all()
    serializer_class = HabilidadesSerializer


class CertificacaoViewSet(viewsets.ModelViewSet):
    queryset = Certificacao.objects.all()
    serializer_class = CertificacaoSerializer
