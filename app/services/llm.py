import os
from dotenv import load_dotenv
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.docling import DoclingReader
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import (
    VectorStoreIndex,
    load_index_from_storage
)
from llama_index.core.memory import ChatSummaryMemoryBuffer
from ..database.chroma import storage_context

load_dotenv()

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
api_key = os.environ['GROQ_KEY']

llm = Groq(model='llama3-70b-8192', api_key=api_key)

reader = DoclingReader()
node_parser = MarkdownNodeParser()
docs = reader.load_data("https://msie-file-67.ezihost.net/")
# docs = reader.load_data("https://pt.wikipedia.org/wiki/Furia_Esports")
vector_index = VectorStoreIndex.from_documents(documents=docs,transformations=[node_parser],embed_model=embed_model, storage_context=storage_context)

def get_prompt(query):
    prompt = f"""
        Você é um assíduo fã da FURIA qualquer pergunta com esse tema você poderá responder isso. Seu nome é Furioso AI,
        especialista em tudo sobre a FURIA, sua função é tirar duvidas(de forma simpatica e natural não cite isso.) sobre qualquer coisa acerca da FURIA
        Gere uma resposta detalhada para a consulta feita com base apenas no contexto obtido:
        Caso forem feitas perguntas de elenco sempre pegue o elenco ativo e atual do ano em que estamos.
        Query: {query}

        Instruções:
        1. Exiba a consulta e a resposta gerada com base no contexto.
        2. Sua resposta deve ser detalhada e abranger todos os aspectos do contexto.
        3. Seja concisa e concisa.
        4. Não inclua mais nada em sua resposta - sem cabeçalho/rodapé/código, etc.
        5. Responda de acordo com a LINGUA(ex: se ele perguntar em portugues responda em portugues.) utilizada pelo usuário.
        6. Caso as perguntas forem sobre lineups da furia responda utlizando as do ano atual, 2025.
        7. Não responda de forma suscinta. Dê muitos detalhes do que foi perguntado.
        """
    return prompt

def generate_response(query):
    chat_engine = vector_index.as_chat_engine(
        mode='CONTEXT', 
        llm=llm, 
        system_prompt=get_prompt(query) 
    )

    response = chat_engine.chat(query)
    return response.response
