from AdenocarcClassifier  import logger
from AdenocarcClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from AdenocarcClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#from AdenocarcClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
#from AdenocarcClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} starged!! <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed!! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e