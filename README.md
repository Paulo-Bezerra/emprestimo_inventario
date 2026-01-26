# Empréstimo de Inventário

![version](https://img.shields.io/badge/Versão-0.1.0-blue)
![status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

O sistema tem como objetivo gerenciar o fluxo de empréstimo de materiais na COAPAC do IFRN/MC (Instituto Federal do Rio Grande do Norte Campus Macau). O sistema contará com um terminal de autoatendimento e um dashboard administrativo, integrando-se ao SUAP para autenticação unificada e notificações.

O projeto está em fase inicial e atualmente contém apenas a configuração de infraestrutura para desenvolvimento.

---

## 📌 Sobre o projeto

Este sistema tem como objetivo registrar e gerenciar empréstimos de itens de inventário (como equipamentos, materiais, etc.), permitindo controle simples e centralizado.

Neste momento, o foco foi a preparação do ambiente de desenvolvimento utilizando Docker e Django.

Caso queira uma visão inicial dos requisitos, acesse [o documento de requisitos](docs/requisitos.md).


---

## 🛠️ Tecnologias utilizadas

- Python 3.14
- Django 5.2 LTS
- Docker
- Docker Compose
- SQLite

---

## 🚀 Como rodar o projeto (desenvolvimento)

### Pré-requisitos

- Docker
- Docker Compose (v2)

### Passos

```bash
git clone https://github.com/Paulo-Bezerra/emprestimo_inventario.git
cd emprestimo_inventario
cp .env.example .env
docker compose up --build
```

Após subir o container, acesse:

[http://localhost:8080](http://localhost:8080)

