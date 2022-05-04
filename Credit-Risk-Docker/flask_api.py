# -*- coding: utf-8 -*-

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
pickle_in = open("bestModel.pkl", "rb")
bestModel = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict', methods=["Get"])
def predict_credit_default():
    """Let's Predict if the user will default payment  
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: LIMIT_BAL
        in: query
        type: number
        required: true
      - name: AGE
        in: query
        type: number
        required: true
      - name: PAY_1
        in: query
        type: number
        required: true
      - name: PAY_2
        in: query
        type: number
        required: true
      - name: PAY_3
        in: query
        type: number
        required: true
      - name: PAY_4
        in: query
        type: number
        required: true
      - name: PAY_5
        in: query
        type: number
        required: true
      - name: PAY_6
        in: query
        type: number
        required: true
      - name: BILL_AMT1
        in: query
        type: number
        required: true
      - name: BILL_AMT2
        in: query
        type: number
        required: true
      - name: BILL_AMT3
        in: query
        type: number
        required: true
      - name: BILL_AMT4
        in: query
        type: number
        required: true
      - name: BILL_AMT5
        in: query
        type: number
        required: true
      - name: BILL_AMT6
        in: query
        type: number
        required: true
      - name: PAY_AMT1
        in: query
        type: number
        required: true
      - name: PAY_AMT2
        in: query
        type: number
        required: true
      - name: PAY_AMT3
        in: query
        type: number
        required: true
      - name: PAY_AMT4
        in: query
        type: number
        required: true
      - name: PAY_AMT5
        in: query
        type: number
        required: true
      - name: PAY_AMT6
        in: query
        type: number
        required: true
      - name: SEX_1
        in: query
        type: number
        required: true
      - name: SEX_2
        in: query
        type: number
        required: true
      - name: EDUCATION_1
        in: query
        type: number
        required: true
      - name: EDUCATION_2
        in: query
        type: number
        required: true
      - name: EDUCATION_3
        in: query
        type: number
        required: true
      - name: EDUCATION_4
        in: query
        type: number
        required: true
      - name: MARRIAGE_1
        in: query
        type: number
        required: true
      - name: MARRIAGE_2
        in: query
        type: number
        required: true
      - name: MARRIAGE_3
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
      
    LIMIT_BAL = request.args.get('LIMIT_BAL')
    AGE = request.args.get('AGE')
    PAY_1 = request.args.get('PAY_1') 
    PAY_2 = request.args.get('PAY_2') 
    PAY_3 = request.args.get('PAY_3') 
    PAY_4 = request.args.get('PAY_4') 
    PAY_5 = request.args.get('PAY_5') 
    PAY_6 = request.args.get('PAY_6')
    BILL_AMT1 = request.args.get('BILL_AMT1') 
    BILL_AMT2 = request.args.get('BILL_AMT2') 
    BILL_AMT3 = request.args.get('BILL_AMT3') 
    BILL_AMT4 = request.args.get('BILL_AMT4') 
    BILL_AMT5 = request.args.get('BILL_AMT5') 
    BILL_AMT6 = request.args.get('BILL_AMT6') 
    PAY_AMT1 = request.args.get('PAY_AMT1') 
    PAY_AMT2 = request.args.get('PAY_AMT2') 
    PAY_AMT3 = request.args.get('PAY_AMT3') 
    PAY_AMT4 = request.args.get('PAY_AMT4') 
    PAY_AMT5 = request.args.get('PAY_AMT5') 
    PAY_AMT6 = request.args.get('PAY_AMT6')
    SEX_1 = request.args.get('SEX_1')
    SEX_2 = request.args.get('SEX_2') 
    EDUCATION_1 = request.args.get('EDUCATION_1')
    EDUCATION_2 = request.args.get('EDUCATION_2') 
    EDUCATION_3 = request.args.get('EDUCATION_3') 
    EDUCATION_4 = request.args.get('EDUCATION_4') 
    MARRIAGE_1 = request.args.get('MARRIAGE_1')
    MARRIAGE_2 = request.args.get('MARRIAGE_2')
    MARRIAGE_3 = request.args.get('MARRIAGE_3')  
    
 
    prediction = bestModel.predict([[LIMIT_BAL, AGE, PAY_1, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5,  PAY_AMT6, SEX_1, SEX_2, EDUCATION_1, EDUCATION_2, EDUCATION_3, EDUCATION_4, MARRIAGE_1, MARRIAGE_2, MARRIAGE_3]])
    return "The Credit Default Predection is" + str(prediction)

#http://127.0.0.1:5000/predict?LIMIT_BAL=1200&SEX_1=1&SEX_2=0&EDUCATION_1=1&EDUCATION_2=0&EDUCATION_3=0&EDUCATION_4=0&MARRIAGE_1=1&MARRIAGE_2=0&MARRIAGE_3=0&AGE=26&PAY_1=-1&PAY_2=-1&PAY_3=-1&PAY_4=-1&PAY_5=-1&PAY_6=-1&BILL_AMT1=2300&BILL_AMT2=1256&BILL_AMT3=2356&BILL_AMT4=1233&BILL_AMT5=2344&BILL_AMT6=3211&PAY_AMT1=2345&PAY_AMT2=2345&PAY_AMT3=2345&PAY_AMT4=2345&PAY_AMT5=2345&PAY_AMT6=2345


    
@app.route('/predict_file', methods=["POST"])
def predict_credit_default1():
    """Let's Predict if the user will default payment 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = bestModel.predict(df_test)
    return "The Credit Default Predictions for the csv is" + str(list(prediction))
    

if __name__ == '__main__':
    #app.run()
	app.run(host='0.0.0.0',port=5000)