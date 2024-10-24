from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from candidatos.views import (
    CandidatoViewSet,
    EnderecoViewSet,
    ContatoViewSet,
    ExperienciaProfissionalViewSet,
    FormacaoAcademicaViewSet,
    HabilidadesViewSet,
    CertificacaoViewSet,
)

# Criando um roteador para o DRF
router = DefaultRouter()
router.register(r"candidatos", CandidatoViewSet)  # Rotas para Candidato
router.register(r"endereco", EnderecoViewSet)  # Rotas para Endereço
router.register(r"contato", ContatoViewSet)  # Rotas para Contato
router.register(
    r"experiencias", ExperienciaProfissionalViewSet
)  # Rotas para Experiência Profissional
router.register(r"formacoes", FormacaoAcademicaViewSet)  # Rotas para Formação Acadêmica
router.register(r"habilidades", HabilidadesViewSet)  # Rotas para Habilidades
router.register(r"certificacoes", CertificacaoViewSet)  # Rotas para Certificações

# URL patterns no projeto principal
urlpatterns = [
    path("admin/", admin.site.urls),  # Rota para o admin
    path("api/", include(router.urls)),  # Inclui todas as rotas do DRF
]
