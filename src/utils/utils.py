import os,sys
from src.logger.logger import logging
from src.exception.exception import CustomException
import pickle
from sklearn.metrics import r2_score,mean_absolute_error

def save_object(file_path,obj):
    try:
        dirname = os.path.dirname(file_path)
        os.makedirs(dirname,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        logging.info("error occured while saving an object")
        raise CustomException(e,sys)
        
        
## function for evaluating the model    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        
        for i in range(len(models)):
            model = list(models.values())[i]
            
            ## Train Model
            model.fit(X_train,y_train)
            
            ## Predict testing data
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            
            ## Get R2 score for both train and test data
            train_r2_score = r2_score(y_train,y_pred_train)
            test_r2_score = r2_score(y_test,y_pred_test)
            
            report[list(models.keys())[i]] = test_r2_score
            
        return report
                    
        
    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)