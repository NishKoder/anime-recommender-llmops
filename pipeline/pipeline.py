from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, GROQ_MODEL_ID
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)


class AnimeRecommenderPipeline:
    def __init__(self, persist_directory: str = "chroma_db"):
        try:
            logger.info("Initializing AnimeRecommenderPipeline...")
            self.vector_store_builder = VectorStoreBuilder(
                csv_file="",
                persist_directory=persist_directory
            )
            self.vector_store_retriever = self.vector_store_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(
                retriever=self.vector_store_retriever,
                api_key=GROQ_API_KEY,
                model_name=GROQ_MODEL_ID
            )
            logger.info("AnimeRecommenderPipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing AnimeRecommenderPipeline: {e}")
            raise CustomException("Failed to initialize AnimeRecommenderPipeline", e)
        
    def recommend(self, query: str):
        """Get anime recommendations based on the query."""
        try:
            logger.info(f"Getting recommendation for query: {query}")
            recommendation = self.recommender.get_recommendation(query)
            logger.info("Recommendation retrieved successfully.")
            return recommendation
        except Exception as e:
            logger.error(f"Error getting recommendation: {e}")
            raise CustomException("Failed to get recommendation", e)