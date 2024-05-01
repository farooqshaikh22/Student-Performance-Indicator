from flask import Flask, request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictionPipeline
import os
from werkzeug.utils import secure_filename
from Prediction.batch import batch_prediction
from src.logger.logger import logging
from src.components.data_transformation import DataTransformationConfig
from src.config.configuration import *
from src.pipeline.training_pipeline import Train
from Prediction.batch import batch_prediction

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
    
@app.route("/batch",methods = ['GET','POST'])
def perform_batch_prediction():
    if request.method=='GET':
        return render_template('batch.html')
    
    else:
        file = request.files['csv_file']  # Update the key to 'csv_file'
        # Directory path
        directory_path = UPLOAD_FOLDER
        # Create the directory
        os.makedirs(directory_path, exist_ok=True)

        # Check if the file has a valid extension
        if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            # Delete all files in the file path
            for filename in os.listdir(os.path.join(UPLOAD_FOLDER)):
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

            # Save the new file to the uploads directory
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            print(file_path)

            logging.info("CSV received and Uploaded")
            
            # Perform batch prediction using the uploaded file
            
            batch = batch_prediction(file_path,model_path,transformer_file_path)
            
            batch.start_batch_prediction()
                       
            output = 'Batch Prediction Done'
                         
            return render_template("batch.html", prediction_result=output, prediction_type='batch')
        else:
            return render_template('batch.html', prediction_type='batch', error='Invalid file type')
            
    
if __name__ == '__main__':
    app.run(debug=True)