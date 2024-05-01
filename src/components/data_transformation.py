from src.constants.constants import *
from src.config.configuration import *
from src.utils.utils import save_object
from src.logger.logger import logging
from src.exception.exception import CustomException
import os,sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


@dataclass
class DataTransformationConfig:
    processor_obj_file_path:str = PROCESSOR_OBJ_FILE_PATH
    transformed_train_data_file_path:str = TRANSFORMED_TRAIN_DATA_FILE_PATH
    transformed_test_data_file_path:str = TRANSFORMED_TEST_DATA_FILE_PATH
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
        
    def get_data_transformation(self):
        
        try:
            logging.info("Data Transformation Started")
            
            ## defining numerical and categorical columns
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            logging.info("Pipeline Initiated") 
            
            ## Numerical Pipeline            
            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),   
                ("scaler",StandardScaler(with_mean=False))
            ])
            
            ## Categorical Pipeline
            cat_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("ohe",OneHotEncoder(handle_unknown='ignore')),
                ("scaler",StandardScaler(with_mean=False))
            ])
            
            preprocessor = ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)
            ])
            
            return preprocessor
            
        
        except Exception as e:
            logging.info("Error Occured in the get_data_transformation")
            raise CustomException(e,sys)
        
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info('read train and test data')
            logging.info(f"Train Dataframe Head : /n {train_df.head().to_string()}")
            logging.info(f"Test Dataframe Head : /n {test_df.head().to_string()}")
            
            logging.info("Obtaining preprocessing object")
            preprocessor_obj = self.get_data_transformation()
            
            target_column_name="math_score"
            
            X_train = train_df.drop(columns=[target_column_name],axis=1)
            y_train = train_df[target_column_name]
            
            X_test = test_df.drop(columns=[target_column_name],axis=1)
            y_test = test_df[target_column_name]
                                  
            logging.info('Applying preprocessor object on train and test data')
            X_train_transformed = preprocessor_obj.fit_transform(X_train)
            X_test_transformed = preprocessor_obj.transform(X_test)
            
            train_array = np.c_[X_train_transformed,np.array(y_train)]
            test_array = np.c_[X_test_transformed,np.array(y_test)]
            
            df_train = pd.DataFrame(train_array)
            df_test = pd.DataFrame(test_array)
            
            os.makedirs(os.path.dirname(
                self.data_transformation_config.transformed_train_data_file_path
                ),exist_ok=True)
            
            df_train.to_csv(self.data_transformation_config.transformed_train_data_file_path,
                            index=False,header=True)
            
            os.makedirs(os.path.dirname(
                self.data_transformation_config.transformed_test_data_file_path
            ),exist_ok=True)
            
            df_test.to_csv(self.data_transformation_config.transformed_test_data_file_path,
                           index=False,header=True)
            
            
            
            save_object(
                file_path=self.data_transformation_config.processor_obj_file_path,
                obj=preprocessor_obj
            )
            logging.info('preprocessor pickle file saved')
                        
            return(
                train_array,
                test_array
            )
            
        except Exception as e:
            logging.info('Exception occured in the initiate_data_transformation')
            raise CustomException(e,sys)