from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb

class ChromaEmbeddingWrapper:
    def __init__(self, model_name): 
        self.model = HuggingFaceEmbedding(model_name=model_name)

    def __call__(self, input):
        return self.model.embed(input)

embed_model_chroma = ChromaEmbeddingWrapper(model_name='sentence-transformers/all-MiniLM-L6-v2')

chroma_client = chromadb.PersistentClient(path='./chroma_db')
collection_name = 'furia_docs'

try:
  chroma_collection = chroma_client.get_or_create_collection(
    name = collection_name,
    embedding_function = embed_model_chroma
  )
except Exception as e:
  print(f'error: {e}')

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)