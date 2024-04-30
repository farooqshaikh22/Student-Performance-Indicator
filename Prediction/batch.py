import os,sys
from src.constants.constants import *
from src.config.configuration import *
from src.utils.utils import load_object
from src.logger.logger import logging
from src.exception.exception import CustomException
import pandas as pd
import pickle

PREDICTION_DIR = 'batch_prediction'
PREDICTION_CSV = 'prediction_csv'
PREDICTION_FILE = 'output.csv'

ROOT_DIR = os.getcwd()
BATCH_PREDICTION = os.path.join(ROOT_DIR,PREDICTION_DIR,PREDICTION_CSV,PREDICTION_FILE)

class batch_prediction:
    def __init__(
        self,
        input_file_path,
        model_file_path,
        transformation_file_path
    ):
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.transformation_file_path = transformation_file_path
        
        def start_batch_prediction(self):
            try:
                ##load data transformation path               
                with open(self.transformation_file_path,'rb') as f:
                    preprocessor = pickle.load(f)
                    
                ## load the model
                model = load_object(filepath=self.model_file_path)
                
                df = pd.read_csv(self.input_file_path)
                
                transformed_data = preprocessor.transform(df)
                
                predictions = model.predict(transformed_data)
                
                df_prediction = pd.DataFrame(predictions,columns=['predictions'])
                
                os.makedirs(BATCH_PREDICTION,exist_ok=True)
                df_prediction.to_csv(BATCH_PREDICTION,index=False)
                
                logging.info("Batch Prediction Done")
                               
                
            except Exception as e:
                logging.info("Error Occured During Batch Prediction")
                raise CustomException(e,sys)

