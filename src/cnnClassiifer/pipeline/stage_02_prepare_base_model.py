from typing import Any
from cnnClassiifer.config.configuration import ConfigurationManager
from cnnClassiifer.components.prepare_base_model import PrepareBaseModel
from cnnClassiifer import logger


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline():

    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully.")
    except Exception as e:
        logger.exception(e)
        raise e