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


@app.route("/predict",methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    
    else:
        data = CustomData(
            gender = str(request.form.get('gender')),
            race_ethnicity = str(request.form.get('race_ethnicity')),
            parental_level_of_education = str(request.form.get('parental_level_of_education')),
            lunch = str(request.form.get('lunch')),
            test_preparation_course = str(request.form.get('test_preparation_course')),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))   
        )
        
        final_new_data = data.get_data_as_data_frame()
        
        predict_pipeline = PredictionPipeline()
        
        pred = predict_pipeline.predict(final_new_data)
        
        return render_template('form.html',final_result = pred[0])
    
if __name__ == '__main__':
    app.run(debug=True)