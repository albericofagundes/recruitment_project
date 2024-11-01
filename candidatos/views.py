from rest_framework import viewsets, generics
from .models import Candidato, ExperienciaProfissional, FormacaoAcademica
from .serializers import (
    CandidatoSerializer,
    CandidatoResumoSerializer,
    ExperienciaProfissionalSerializer,
    FormacaoAcademicaSerializer,
)


class ExperienciaProfissionalViewSet(viewsets.ModelViewSet):
    queryset = ExperienciaProfissional.objects.all()
    serializer_class = ExperienciaProfissionalSerializer


class FormacaoAcademicaViewSet(viewsets.ModelViewSet):
    queryset = FormacaoAcademica.objects.all()
    serializer_class = FormacaoAcademicaSerializer


class CandidatoListAllView(generics.ListAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer


class CandidatoListView(generics.ListAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoResumoSerializer
