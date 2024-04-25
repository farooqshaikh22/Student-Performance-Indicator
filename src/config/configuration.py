from src.constants.constants import *

## root directory
ROOT_DIR = ROOT_DIR_KEY

## dataset directory
DATASET_PATH = os.path.join(ROOT_DIR,DATA_DIR,DATA)


## Data Ingestion

RAW_DATA_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_DIR,CURRENT_TIME_STAMP,
                             RAW_DATA_DIR,RAW_DATA)

TRAIN_DATA_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_DIR,CURRENT_TIME_STAMP,
                               INGESTED_DATA_DIR,
                               TRAIN_DATA)

TEST_DATA_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_DIR,CURRENT_TIME_STAMP,
                              INGESTED_DATA_DIR,
                              TEST_DATA)


## Data Transformation

PROCESSOR_OBJ_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_DIR,
                                       PROCESSOR_DIR,PROCESSOR_OBJ)


TRANSFORMED_TRAIN_DATA_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_DIR,
                                                TRANSFORMATION_DIR,TRANSFORMED_TRAIN_DATA)

TRANSFORMED_TEST_DATA_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_DIR,
                                                TRANSFORMATION_DIR,TRANSFORMED_TEST_DATA)


## Model Trainer

MODEL_OBJ_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,MODEL_TRAINER_DIR,MODEL_OBJ)