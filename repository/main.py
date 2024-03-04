from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import messages_to_prompt, completion_to_prompt
from llama_index.llms.openai import OpenAI
from llama_index.core import ServiceContext
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.callbacks import LlamaDebugHandler, CallbackManager
from .ingestion import DataIngestion


class RunRag:
    def __init__(self):
        self.embed_model_name = "BAAI/bge-large-en-v1.5"
        self.embed_model_kwargs = {'device': 'cuda'}
        self.embed_encode_kwargs = {'normalize_embeddings': True}
        self.llm_model_path = r"D:\mistral-7b-instruct-v0.2.Q4_K_M.gguf"
        self.ingestion = DataIngestion()

    def load_embed_model(self):
        try:
            embed_model = HuggingFaceBgeEmbeddings(
                model_name=self.embed_model_name,
                model_kwargs=self.embed_model_kwargs,
                encode_kwargs=self.embed_encode_kwargs,
                query_instruction="Represent this sentence for searching relevant passages: "
            )
            embed_model = LangchainEmbedding(embed_model, embed_batch_size=100)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print("Using OPENAI embedding model..")
            embed_model = OpenAIEmbedding(model="text-embedding-ada-002", embed_batch_size=100)
        return embed_model

    def load_llm_model(self):
        try:
            llm = LlamaCPP(
                # You can pass in the URL to a GGML model to download it automatically
                model_path=self.llm_model_path,
                # optionally, you can set the path to a pre-downloaded model instead of model_url
                temperature=0.2,
                max_new_tokens=512,
                context_window=8000,
                generate_kwargs={},
                model_kwargs={"n_gpu_layers": 35},
                messages_to_prompt=messages_to_prompt,
                completion_to_prompt=completion_to_prompt,
                verbose=True)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print("Using OPENAI LLM model..")
            llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
        return llm

    @staticmethod
    def build_service_context(llm, embed_model):
        node_parser = SimpleNodeParser.from_defaults(chunk_size=256, chunk_overlap=10)
        llama_debug = LlamaDebugHandler(print_trace_on_end=True)
        callback_manager = CallbackManager(handlers=[llama_debug])
        service_context = ServiceContext.from_defaults(
            llm=llm,
            embed_model=embed_model,
            node_parser=node_parser,
            callback_manager=callback_manager
        )
        return service_context


    def run(self):
        embed_model = self.load_embed_model()
        llm = self.load_llm_model()
        service_context = self.build_service_context(llm, embed_model)
        index = self.ingestion.build_vector_store(service_context)
        return index, service_context
