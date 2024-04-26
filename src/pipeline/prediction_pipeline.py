from src.constants.constants import *
from src.config.configuration import *
from src.utils.utils import save_object,evaluate_model,load_object
from src.logger.logger import logging
from src.exception.exception import CustomException
import os,sys
import numpy as np
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path = MODEL_OBJ_FILE_PATH
            processor_path = PROCESSOR_OBJ_FILE_PATH
            
            model = load_object(model_path)
            processor = load_object(processor_path)
            
            data_scaled = processor.transform(features)
            pred = model.predict(data_scaled)
            
            return pred
        
        except Exception as e:
            logging.info("Error Occured in Prediction Pipeline")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(
        self,
        gender:str,
        race_ethnicity:str,
        parental_level_of_education:str,
        lunch:str,
        test_preparation_course:str,
        reading_score:int,
        writing_score:int
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'gender':[self.gender],
                'race_ethnicity':[self.race_ethnicity],
                'parental_level_of_education':[self.parental_level_of_education],
                'lunch':[self.lunch],
                'test_preparation_course':[self.test_preparation_course],
                'reading_score':[self.reading_score],
                'writing_score':[self.writing_score]                               
            }
            
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("Dataframe Gathered")
            
            return df
                
        except Exception as e:
            logging.info("Error Occured in Custom Pipeline Dataframe")
            raise CustomException(e,sys)
        
        
    