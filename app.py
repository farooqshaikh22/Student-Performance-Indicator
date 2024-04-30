from flask import Flask, request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictionPipeline
import os
from werkzeug.utils import secure_filename
from Prediction.batch import batch_prediction
from src.logger.logger import logging
from src.components.data_transformation import DataTransformationConfig
from src.config.configuration import *
from src.pipeline.training_pipeline import Train

transformer_file_path = PROCESSOR_OBJ_FILE_PATH
model_path = MODEL_OBJ_FILE_PATH

UPLOAD_FOLDER = 'batch_prediction/uploaded_csv_file'

app = Flask(__name__,template_folder='templates')

ALLOWED_EXTENSIONS = {'csv'}

@app.route("/")
def home_page():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)