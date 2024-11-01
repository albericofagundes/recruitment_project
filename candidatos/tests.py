from django.test import TestCase
from .models import Candidato, DadosPessoais, Contato


class CandidatoModelTest(TestCase):

    def setUp(self):
        # Criação de instâncias de DadosPessoais e Contato para teste
        dados_pessoais = DadosPessoais.objects.create(
            nome="João Silva",
            data_nascimento="1990-01-01",
            nacionalidade="Brasileiro",
            estado_civil="Solteiro",
        )
        contato = Contato.objects.create(
            email="joao.silva@example.com", telefone="(11) 1234-5678"
        )

        # Criação de uma instância de Candidato com relações
        Candidato.objects.create(
            dados_pessoais=dados_pessoais, contato=contato, cargo="Desenvolvedor"
        )

    def test_candidato_tem_dados_completos(self):
        # Testa se todos os candidatos têm dados_pessoais e contato associados
        for candidato in Candidato.objects.all():
            self.assertIsNotNone(
                candidato.dados_pessoais, "Candidato sem dados pessoais"
            )
            self.assertIsNotNone(candidato.contato, "Candidato sem contato")
