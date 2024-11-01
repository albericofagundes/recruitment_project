from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from candidatos.views import (
    ExperienciaProfissionalViewSet,
    FormacaoAcademicaViewSet,
    CandidatoListView,
    CandidatoListAllView,
)

router = DefaultRouter()
router.register(r"experiencias-profissionais", ExperienciaProfissionalViewSet)
router.register(r"formacoes-academicas", FormacaoAcademicaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("candidatos/", CandidatoListView.as_view(), name="candidato-list"),
    path("candidatos-all/", CandidatoListAllView.as_view(), name="candidato-list-all"),
]
