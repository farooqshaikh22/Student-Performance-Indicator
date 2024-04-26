from src.constants.constants import *
from src.config.configuration import *
from src.utils.utils import save_object,evaluate_model
from src.logger.logger import logging
from src.exception.exception import CustomException
import os,sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet,SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score,mean_absolute_error

@dataclass
class ModelTrainerConfig:
    model_obj_file_path:str = MODEL_OBJ_FILE_PATH
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info('Splitting dependant and independant variables from train and test data')
            
            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            
            models = {
                    'LinearRegression':LinearRegression(),
                    'Lasso':Lasso(),
                    'Ridge':Ridge(),
                    'Elasticnet':ElasticNet(),
                    'SGD':SGDRegressor(),
                    'Decision Tree' :DecisionTreeRegressor(),
                    'KNN':KNeighborsRegressor(),
                    'XBG':XGBRegressor(),
                    'RandomForest':RandomForestRegressor(),
                    'Adaboost':AdaBoostRegressor(),
                    'Gradientboost':GradientBoostingRegressor()
            }
            
            model_report:dict = evaluate_model(X_train,y_train,X_test,y_test,models)
            
            print(model_report)
            print("\n=======================================================================\n")
            logging.info(f"Model Report : {model_report}")
            
            ##Get best model score from dictionary
            best_model_score = max(sorted(model_report.values()))
            
            ## To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                ]
            
            best_model = models[best_model_name]
            
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            print(f'Best Model Found , Model Name : {best_model_name},R2 Score : {best_model_score}')
            print('\n========================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name},R2 Score : {best_model_score}')
            
            save_object(
                file_path=self.model_trainer_config.model_obj_file_path,
                obj=best_model
                )
                

        
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)