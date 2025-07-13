from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()


class VectorStoreBuilder:
    def __init__(self, csv_file: str, persist_directory: str = "chroma_db"):
        self.csv_file = csv_file
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def build_and_save_vector_store(self):
        """Builds a vector store from the CSV file."""
        # Load the CSV file
        loader = CSVLoader(file_path=self.csv_file, encoding='utf-8')
        documents = loader.load()

        # Split the text into chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(documents)

        # Create the vector store
        vector_store = Chroma.from_documents(
            split_docs,
            self.embeddings,
            persist_directory=self.persist_directory
        )

    def load_vector_store(self):
        """Loads the vector store from the persisted directory."""
        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )