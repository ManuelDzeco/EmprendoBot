import os
import datetime
import google.generativeai as genai
import gspread
from dotenv import load_dotenv

# Carregar variáveis de ambient
load_dotenv()

# Configurar Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Configurar Google Sheets
gc = gspread.service_account(filename="credenciais/emprendobot-credentials.json")
sheet = gc.open_by_key(os.getenv("SHEET_ID")).sheet1

# Estruturas de contexto por usuário
user_context = {}

# Histórico da conversa: lista de tuplas (autor, texto)
history = [
    ("system",
     "Você é o EmprendoBot, um mentor criativo de negócios moçambicanos. Seu objetivo é apoiar pequenos empreendedores com dicas práticas e, caso precise de mais informações, faça perguntas de follow-up ao usuário para entender melhor seu negócio e desafio.")
]

def registrar_interacao(dados: dict):
    """Salva a interação no Google Sheets."""
    row = [
        dados.get('user_id', ''),
        dados.get('nome', ''),
        dados.get('negocio', ''),
        dados.get('desafio', ''),
        dados.get('dica', ''),
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]
    try:
        sheet.append_row(row)
    except Exception as e:
        print(f"[ERRO] Não foi possível salvar no Sheets: {e}")


def build_prompt(user_input: str) -> str:
    """
    Constrói um prompt único a partir do histórico e da entrada do usuário.
    """
    # Atualiza histórico com a entrada do usuário
    history.append(("user", user_input))
    # Concatena todas as mensagens em um único prompt
    prompt = []
    for role, text in history:
        prefix = "Usuário:" if role == "user" else ("Bot:" if role == "assistant" else "Sistema:")
        prompt.append(f"{prefix} {text}")
    prompt.append("Bot:")  # esperando resposta
    return "\n".join(prompt)


def chat_loop():
    """Loop de conversa fluida usando generate_content."""
    print("🤖 Bem-vindo ao EmprendoBot! Vamos conversar sobre seu negócio. (Digite 'sair' para encerrar)\n")
    user_id = input("> Insira o seu identificador (ex: email ou número) para personalização:\n").strip()
    if user_id.lower() in ['sair', 'exit', 'quit']:
        print("Até logo!")
        return
    name_input = input("> Qual é o seu nome?\n").strip()
    if name_input.lower() in ['sair', 'exit', 'quit']:
        print("Até logo!")
        return
    nome = name_input

    # Armazenar nome no histórico
    history.append(("user", f"Meu nome é {nome}."))
    # Inicializa dicionário para armazenar dados do usuário
    dados = {'user_id': user_id, 'nome': nome, 'negocio': None, 'desafio': None, 'dica': None}

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("🤖 Até logo! Sucesso no seu empreendimento.")
            break

        # Constrói prompt para o Gemini
        prompt = build_prompt(user_input)

        # Gera resposta única
        try:
            response = model.generate_content(prompt)
            bot_reply = response.text.strip()
        except Exception as e:
            print(f"[ERRO] Falha ao gerar resposta: {e}")
            continue

        # Exibe resposta
        print(f"🤖 {bot_reply}\n")
        # Registra resposta no histórico
        history.append(("assistant", bot_reply))

        # Extração simples de dados
        if dados['negocio'] is None and 'negócio' in user_input.lower():
            dados['negocio'] = user_input
        if dados['desafio'] is None and ('desafio' in user_input.lower() or 'orientação' in user_input.lower()):
            dados['desafio'] = user_input
        if dados['dica'] is None and bot_reply:
            dados['dica'] = bot_reply

        # Se tiver todos, salva e mantém nome para próxima rodada
        if all([dados['user_id'],dados['nome'], dados['negocio'], dados['desafio'], dados['dica']]):
            registrar_interacao(dados)
            # Prepara novo ciclo mantendo nome
            dados = {'negocio': None, 'desafio': None, 'dica': None}


if __name__ == "__main__":
    chat_loop()
