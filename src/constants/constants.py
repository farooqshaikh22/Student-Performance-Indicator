import os,sys
from datetime import datetime


def current_time_stamp():
    
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = current_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = 'data'
DATA = 'stud.csv'

ARTIFACT_DIR_KEY = 'artifact'

## data ingestion related variables

DATA_INGESTION_DIR = 'data_ingestion'
INGESTED_DATA_DIR = 'ingested_data'
RAW_DATA_DIR = 'raw_data'
RAW_DATA = 'data.csv'
TRAIN_DATA = 'train.csv'
TEST_DATA = 'test.csv'