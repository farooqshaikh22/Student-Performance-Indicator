from src.constants.constants import *
from src.config.configuration import *
from src.logger.logger import logging
from src.exception.exception import CustomException
import os,sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str = RAW_DATA_PATH
    train_data_path:str = TRAIN_DATA_PATH
    test_data_path:str = TEST_DATA_PATH
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(DATASET_PATH)
            logging.info("Read the Dataset as Dataframe")
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("train test split initiated")
            train_data_set,test_data_set = train_test_split(df,test_size=0.2,random_state=42)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train_data_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test_data_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data Ingestion Completed")
            
            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
            
            
        except Exception as e:
            logging.info("Exception Occured in initiate_data_ingestion")
            raise CustomException(e,sys)

if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()