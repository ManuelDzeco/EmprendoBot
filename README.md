# 🎉 EmprendoBot: Seu Mentor de Negócios em Moçambique 🚀

**EmprendoBot** é mais que um chatbot: é a bússola digital que guia pequenos empreendedores moçambicanos rumo ao sucesso, usando o poder da IA do Gemini e a flexibilidade do Google Sheets. Com ele, cada usuário tem um mentor 24/7, pronto para inspirar, instruir e registrar seu progresso.

---

## 💡 Por que o EmprendoBot é Único?

* **Personalização Total**: Cada empreendedor acessa apenas suas próprias interações, garantindo privacidade e foco.
* **Diálogo Fluido**: O EmprendoBot faz perguntas de follow-up inteligentes, entendendo seu negócio e desafio de forma natural — sem prompts rígidos.
* **Criatividade Local**: Inspirações, dicas e exemplos ancorados na cultura moçambicana, com sugestões de baixo custo e alto impacto.
* **Memória Ativa**: Armazena automaticamente nome, tipo de negócio, desafio e dicas em uma planilha Google, que você pode consultar e transformar em insights.

---

## 🏆 Em Partida para o Concurso Alura AI

Este projeto foi criado para a **Imersão Alura de Inteligência Artificial**, e concorre ao destaque como ideia mais inovadora e impactante para Moçambique.

> **Meta:** Empoderar 100 microempreendedores nos próximos 30 dias, transformando sonhos em planos de ação concretos.

---

## ⚙️ Tecnologias e Ferramentas

* **Google Generative AI (Gemini)**: cérebro do mentor criativo.
* **Google Sheets API & gspread**: banco de dados gratuito e acessível.
* **Python & dotenv**: simplicidade e segurança na configuração.
* **Possível Futuro**: FastAPI para deploy gratuito, Telegram Bot para alcance instantâneo.

---

## 🚀 Como Usar

1. **Clone o repositório**

   ```bash
   git clone git@github.com:<seu-usuario>/EmprendoBot.git
   cd EmprendoBot
   ```
2. **Configure o ambiente**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
3. **Prepare as credenciais**

   * Crie um `.env` com suas chaves:

     ```dotenv
     GOOGLE_API_KEY=<sua_api_key_gemini>
     SERVICE_ACCOUNT_FILE=service_account.json
     SHEET_ID=<seu_sheet_id>
     ```
   * Coloque o `service_account.json` na raiz.
4. **Inicie o EmprendoBot**

   ```bash
   python chatbot.py
   ```
5. **Interaja naturalmente**

   * Apresente-se (seu nome e identificador).

* Explique seu negócio e desafio em uma frase.
* Receba dicas criativas e personalize o diálogo com perguntas de follow-up.

---

## 📈 Próximos Passos e Roadmap

* **Ponto 6**: Multi-idioma com Google Translate API.
* **Ponto 1**: Deploy gratuito com FastAPI (Vercel/Heroku).
* **Ponto 2**: Integração com Telegram para alcance instantâneo.
* **Dashboard**: Relatórios no Data Studio, acesso restrito ao empreendedor via email.

---

## 🙌 Contribua e Faça História!

Gostaria de ver novas funcionalidades ou ajudar a escalar o projeto?

1. Crie uma *issue* descrevendo sua ideia.
2. Abra um *pull request* com melhorias.

Juntos, podemos transformar o ecossistema de microempreendimentos em Moçambique!

---

<p align="center">Feito com ❤️ para Moçambique — Imersão Alura AI 2025</p>
