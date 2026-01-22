# Python 3.14.2 sobre Debian 13 (Trixie), versão slim
FROM python:3.14.2-slim-trixie

# Evita criar arquivos .pyc e garante logs imediatos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências de sistema necessárias para psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o código da aplicação
COPY . .

# Cria a pasta 'data' caso não exista (necessário para SQLite)
RUN mkdir -p /app/data