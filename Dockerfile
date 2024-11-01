# Usa a imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos do projeto para o contêiner
COPY requirements.txt .

# Instala as dependências do Django
RUN pip install -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . .

# Define a variável de ambiente para o Django
ENV DJANGO_SETTINGS_MODULE=seuprojeto.settings

# Executa o comando para iniciar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
