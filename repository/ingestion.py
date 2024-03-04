import os
from .preprocessing import DataPreprocessing
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage


class DataIngestion:
    def __init__(self):
        self.preprocessing = DataPreprocessing()

    def build_vector_store(self, service_context):
        csv_dir = os.path.join('data/raw_data', 'SPOTIFY_REVIEWS.csv')
        persist_dir = os.path.join('data', 'vector_storage')
        if not os.path.exists(persist_dir):
            self.preprocessing.clean_review_text(csv_dir)
            documents = SimpleDirectoryReader("data/clean_data").load_data()
            print('BUILDING VECTOR STORE...')
            index = VectorStoreIndex.from_documents(documents=documents,
                                                    service_context=service_context,
                                                    show_progress=True)
            index.storage_context.persist(persist_dir=persist_dir)
        else:
            storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
            index = load_index_from_storage(storage_context, service_context=service_context)
        return index
