import os,sys
from src.constants.constants import *
from src.config.configuration import *
from src.logger.logger import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class Train:
    def __init__(self):
        self.c = 0
        print(f"********************************{self.c}************************************")
        
        
    def main(self):
        obj = DataIngestion()
        train_data_path,test_data_path = obj.initiate_data_ingestion()
        
        data_transformation = DataTransformation()
        train_arr,test_arr = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(train_arr,test_arr)
