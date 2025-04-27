# FURIOSO AI API
API do Chatbot da [FURIA](https://furia.gg)

## Sobre o projeto 📜
No Chatbot API você consegue
- Fazer request para perguntar qualquer coisa sobre a furia

Foi construido com:
- Python 3
- LlamaIndex
    - Groq
- FastAPI
- ChromaDB

## Instalando o projeto 📦
Pré-requisitos:
- [Python 3](https://www.python.org/downloads/)
- [Groq API KEY](https://groq.com)
    - Crie uma apikey no groq para utilizar a LLM

Clone o repositório para a sua maquina local:
Com Https:

```bash
git clone https://github.com/jpbrab0/chatbot-furia.git
```

Com SSH:

```bash
git clone git@github.com:jpbrab0/chatbot-furia.git
```

Com Github CLI:

```bash
gh repo clone jpbrab0/chatbot-furia
```

## Rodando o projeto 🏃
1. Acesse o diretório do projeto:
- `cd chatbot-furia`

2. Inicie um virtual environment com o python:

- `python3 -m venv env`

3. Acesse o virtual environment:
- `source env/bin/activate`

4. Instale as dependencias(vai demorar um pouco por conta o LlamaIndex)
- `pip install -r requirements.txt`

5. Renomeie o .env.example para .env:

- `mv .env.example .env`

6. No .env, adicione a sua api key do Groq:
- `GROQ_KEY=<sua key>`

7. Inicie o server
- `fastapi dev app/main.py` ou `uvicorn app.main:app --host 127.0.0.1 --port 8000`

8. Acesse localmente:
- `http://127.0.0.1:8000`

## Endpoints
Url base: `https://127.0.0.1:8000`

### Fazer uma query

```http
POST /api/chat
```

| Parametro | Tipo   |
| :-------- | :----- |
| `query`      | `string` |

Feito por [jpbrab0](https://github.com/jpbrab0)