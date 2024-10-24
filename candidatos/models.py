from django.db import models


class Candidato(models.Model):
    nome = models.CharField(
        max_length=100
    )  # Validar que não é vazio e não tem caracteres especiais
    sobrenome = models.CharField(max_length=100, blank=True)  # Sobrenome opcional
    data_nascimento = models.DateField()  # Validar data no passado (maior de idade)
    cpf = models.CharField(max_length=11, unique=True)  # Validar formato e dígitos
    rg = models.CharField(max_length=20, unique=True)  # Validar formato e dígitos
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)  # Opcional
    estado_civil = models.CharField(
        max_length=20,
        choices=[
            ("solteiro", "Solteiro(a)"),
            ("casado", "Casado(a)"),
            ("divorciado", "Divorciado(a)"),
            ("viuvo", "Viúvo(a)"),
            ("união_estável", "União Estável"),
        ],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Endereco(models.Model):
    candidato = models.OneToOneField(
        Candidato, on_delete=models.CASCADE, related_name="endereco"
    )
    rua = models.CharField(max_length=255)  # Não permitir vazio
    numero = models.CharField(
        max_length=10, null=True, blank=True
    )  # Validar se é numérico
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(
        max_length=10, null=True, blank=True
    )  # Validar formato (#####-###)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    pais = models.CharField(
        max_length=50, default="Brasil"
    )  # Definir como Brasil por padrão

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"


class Contato(models.Model):
    candidato = models.OneToOneField(
        Candidato, on_delete=models.CASCADE, related_name="contato"
    )
    email = models.EmailField(unique=True)  # Email com validação interna do Django
    telefone_celular = models.CharField(
        max_length=20
    )  # Validar formato (##) ####-#### ou similar
    telefone_fixo = models.CharField(
        max_length=20, null=True, blank=True
    )  # Validação similar ao celular

    def __str__(self):
        return f"{self.candidato.nome} - {self.email}"


class ExperienciaProfissional(models.Model):
    candidato = models.ForeignKey(
        Candidato, on_delete=models.CASCADE, related_name="experiencias"
    )
    cargo = models.CharField(max_length=100)  # Não permitir vazio
    empresa = models.CharField(max_length=100)  # Não permitir vazio
    data_inicio = models.DateField()  # Validar data no passado
    data_fim = models.DateField(
        null=True, blank=True
    )  # Validar que seja depois de `data_inicio`
    descricao = models.TextField(blank=True)
    responsavel = models.CharField(max_length=100, null=True, blank=True)
    contato_responsavel = models.CharField(
        max_length=20, null=True, blank=True
    )  # Validar telefone
    habilidades_utilizadas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.candidato.nome} - {self.cargo} na {self.empresa}"


class FormacaoAcademica(models.Model):
    candidato = models.ForeignKey(
        Candidato, on_delete=models.CASCADE, related_name="formacoes"
    )
    instituicao = models.CharField(max_length=100)  # Não permitir vazio
    curso = models.CharField(max_length=100)  # Não permitir vazio
    data_inicio = models.DateField()  # Validar data no passado
    data_fim = models.DateField(
        null=True, blank=True
    )  # Validar que seja depois de `data_inicio`
    nota_final = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )  # Validar que seja 0-10
    tipo = models.CharField(
        max_length=20,
        choices=[
            ("tecnico", "Técnico"),
            ("graduacao", "Graduação"),
            ("pos_graduacao", "Pós-graduação"),
            ("especializacao", "Especialização"),
            ("mestrado", "Mestrado"),
            ("doutorado", "Doutorado"),
        ],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.candidato.nome} - {self.curso} na {self.instituicao}"


class Habilidades(models.Model):
    candidato = models.ForeignKey(
        Candidato, on_delete=models.CASCADE, related_name="habilidades"
    )
    nome = models.CharField(max_length=100)  # Não permitir vazio
    nivel = models.CharField(
        max_length=20,
        choices=[
            ("basico", "Básico"),
            ("intermediario", "Intermediário"),
            ("avancado", "Avançado"),
            ("expert", "Expert"),
        ],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.nome} - {self.nivel}"


class Certificacao(models.Model):
    candidato = models.ForeignKey(
        Candidato, on_delete=models.CASCADE, related_name="certificacoes"
    )
    nome_certificacao = models.CharField(max_length=100)  # Não permitir vazio
    instituicao_emissora = models.CharField(max_length=100)  # Não permitir vazio
    data_emissao = models.DateField()  # Validar que seja no passado
    data_validade = models.DateField(
        null=True, blank=True
    )  # Se fornecido, deve ser após `data_emissao`

    def __str__(self):
        return f"{self.nome_certificacao} - {self.instituicao_emissora}"
