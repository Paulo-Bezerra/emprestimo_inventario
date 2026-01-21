# Documento de Especificação de Requisitos de Software

## Sistema de Gerenciamento de Empréstimos da COAPAC/MC/IFRN
**Versão:** 0.0.000 
**Status:** Rascunho Inicial  
**Data:** 25/11/2025

---

## Visão Geral e Arquitetura
O sistema tem como objetivo gerenciar o fluxo de empréstimo de materiais na COAPAC do IFRN/MC (Instituto Federal do Rio Grande do Norte Campus Macau). O sistema contará com um terminal de autoatendimento e um dashboard administrativo, integrando-se ao SUAP para autenticação unificada e notificações.

### 1.1 Diagrama de Arquitetura

![Diagrama de Arquitetura](https://github.com/user-attachments/assets/e006cf6f-36c4-4e3d-b37f-1753bede7b2e)

---

## 1.2 Componentes do Sistema

| Componente            | Descrição                                                               | Sugestão Tecnológica                              |
|-----------------------|-------------------------------------------------------------------------|---------------------------------------------------|
| **Terminal (Tablet)** | Interface simplificada para solicitação de materiais.                   | React (Web App), Flutter ou Django (HTML).        |
| **Dashboard Admin**   | Gestão de estoque, aprovação de pedidos e relatórios.                   | React, Vue.js ou Django Admin.                    |
| **Backend (API)**     | Regras de negócio e integração com SUAP.                                | Python (Django Monólito).                         |
| **Banco de Dados**    | Armazenamento persistente e cache.                                      | PostgreSQL ou SQLite.                             |
| **Integração SUAP**   | Comunicação com a API institucional.                                    | API SUAP ou HTTP direto.                          |

---

## Requisitos Funcionais (RF)

- **RF01 – Autenticação Integrada (SUAP):** Autenticar via SUAP recuperando dados básicos.  
- **RF02 – Consulta de Materiais:** Exibir materiais disponíveis.  
- **RF03 – Solicitação de Empréstimo:** Seleção de material e data.  
- **RF04 – Registrar Solicitação:** Registrar como pendente.  
- **RF05 – Dashboard de Avaliação:** Admin visualiza pendentes.  
- **RF06 – Aprovação:** Admin aprova solicitações.  
- **RF07 – Rejeição:** Admin rejeita solicitações.  
- **RF08 – Gestão de Status:** pendente → aprovado → retirado → devolvido/atrasado.  
- **RF09 – Registro de Retirada.**  
- **RF10 – Registro de Devolução.**  
- **RF11 – Controle de Estoque.**  
- **RF12 – Histórico por matrícula SUAP.**  
- **RF13 – Alertas de Atraso.**  
- **RF14 – CRUD de Materiais.**  
- **RF15 – Notificação Interna (Dashboard).**  
- **RF16 – Notificação via SUAP ou email.**  
- **RF17 – Gestão de Permissões (ACL).**  

---

## Requisitos Não Funcionais (RNF)

- **RNF01 – Usabilidade:** Interface simplificada para o tablet.  
- **RNF02 – Disponibilidade:** Operar em horário comercial.  
- **RNF03 – Desempenho:** API < 2s.  
- **RNF04 – Segurança:** HTTPS + tokens protegidos.  
- **RNF05 – Integridade:** Bloqueio de empréstimos sem estoque.  
- **RNF06 – Resiliência:** Preenchimento do formulário com SUAP fora.  
- **RNF07 – Escalabilidade:** 7,5 mil de registros por ano.  
- **RNF08 – Compatibilidade:** Navegadores modernos.  
- **RNF09 – Auditoria:** Registro dos responsáveis pela autorização.  
- **RNF10 – Privacidade:** Adequação à LGPD.  

---

## Regras de Negócio (RN)

- **RN01:** Empréstimo requer aprovação humana.  
- **RN02:** Estoque nunca pode ser negativo.  
- **RN03:** Atraso altera status automaticamente.  
- **RN04:** Limite depende do perfil SUAP.  
- **RN05:** Itens valiosos exigem validação extra.  
- **RN06:** Usuários com pendências não podem solicitar.  
- **RN07:** Não pode renovar sem devolver.  
- **RN08:** Retirada exige presença física (exceto professores).  
- **RN09:** Campos preenchidos automaticamente via SUAP.  
- **RN10:** Usuários irregulares podem ser bloqueados.  

---

## Modelagem de Dados (ERD)

![Modelagem de Dados](https://github.com/user-attachments/assets/94fd4e5a-92dc-4704-a57e-6395d9cfc50a)

---

## Definição da API (Principais Endpoints)

| Método   | Rota                          | Descrição                        |
|----------|-------------------------------|----------------------------------|
| **GET**  | /auth/suap/login              | Inicia fluxo OAuth2              |
| **POST** | /auth/suap/callback           | Recebe token do SUAP             |
| **GET**  | /materiais                    | Lista materiais                  |
| **POST** | /materiais                    | Cadastra novo material           |
| **POST** | /emprestimos/solicitar        | Cria nova solicitação            |
| **GET**  | /emprestimos                  | Listar empréstimos (com filtros) |
| **PATCH**| /emprestimos/{id}/status      | Atualiza status                  |
| **POST** | /emprestimos/{id}/devolver    | Processa devolução               |

---

## Histórias de Usuário & Critérios de Aceite

### Épico 1: Integração e Acesso

#### HU01 – Login Unificado
- **Dado** que clico em *"Entrar com SUAP"*  
- **Quando** insiro matrícula e senha  
- **Então** o sistema carrega minha foto e nome automaticamente.

---

### Épico 2: Autoatendimento

#### HU03 – Solicitação
- **Dado** que estou logado  
- **Quando** solicito um *Cabo HDMI*  
- **Então** o sistema registra o empréstimo vinculado à minha matrícula SUAP.

---

### Épico 3: Gestão Administrativa

#### HU08 – Aprovação
- **Dado** uma solicitação pendente  
- **Quando** aprovo  
- **Então** o sistema envia uma notificação ao aluno.

#### HU15 – Controle de Permissões
- **Dado** que sou gestor  
- **Quando** busco um usuário  
- **Então** posso marcar **is_admin**.

---

## Roadmap e Melhorias Futuras

- Relatório de não devolvidos.  
- Estaticas de uso no dashboard.  
