import os,sys
from src.logger.logger import logging
from src.exception.exception import CustomException
import pickle

def save_object(file_path,obj):
    try:
        dirname = os.path.dirname(file_path)
        os.makedirs(dirname,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        logging.info("error occured while saving an object")
        raise CustomException(e,sys)
        
    