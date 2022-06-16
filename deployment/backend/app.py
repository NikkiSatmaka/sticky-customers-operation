#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

import joblib
import numpy as np
import pandas as pd
from pathlib import Path

from tensorflow import keras

from packages.imputation_handling import impute_total_charges
from packages.imputation_handling import impute_no_phone_internet


app = Flask(__name__)

# initiate model & columns
LABEL = ["Not Churn", "Churn"]

# set threshold for prediction
THRESHOLD = 0.5

# model location
model_dir = 'models'
scaler_name = 'scaler.pkl'
encoder_name = 'encoder.pkl'
model_name = 'keras_model.h5'

# create path object
scaler_path = Path(model_dir, scaler_name)
encoder_path = Path(model_dir, encoder_name)
model_path = Path(model_dir, model_name)

# load model
scaler = joblib.load(scaler_path)
encoder = joblib.load(encoder_path)
model = keras.models.load_model(model_path)

@app.route("/")
def welcome():
    return "<h3>This is the Backend for My Modeling Program</h3>"

@app.route("/predict", methods=["GET", "POST"])
def predict_churn():
    if request.method == "POST":
        content = request.json
        try:
            # create dictionary to store input data
            new_data = {
                "gender": content["gender"],
                "SeniorCitizen": content["SeniorCitizen"],
                "Partner": content["Partner"],
                "Dependents": content["Dependents"],
                "tenure": content["tenure"],
                "PhoneService": content["PhoneService"],
                "MultipleLines": content["MultipleLines"],
                "InternetService": content["InternetService"],
                "OnlineSecurity": content["OnlineSecurity"],
                "OnlineBackup": content["OnlineBackup"],
                "DeviceProtection": content["DeviceProtection"],
                "TechSupport": content["TechSupport"],
                "StreamingTV": content["StreamingTV"],
                "StreamingMovies": content["StreamingMovies"],
                "Contract": content["Contract"],
                "PaperlessBilling": content["PaperlessBilling"],
                "PaymentMethod": content["PaymentMethod"],
                "MonthlyCharges": content["MonthlyCharges"],
                "TotalCharges": content["TotalCharges"]
            }

            # convert to dataframe
            new_data = pd.DataFrame([new_data])

            # impute missing values
            prepared_data = impute_total_charges(new_data)

            # impute no phone service and no internet service with no
            prepared_data = impute_no_phone_internet(prepared_data)

            # scale data
            scaled_data = scaler.transform(prepared_data)

            # encode data and cast it as float32
            encoded_data = encoder.transform(scaled_data).astype(np.float32)

            # predict and store result
            res = model.predict(encoded_data).reshape(-1)
            res = np.where(res > THRESHOLD, 1, 0)

            # convert result to dictionary
            result = {
                "class": str(res[0]),
                "class_name": LABEL[res[0]]
            }

            # jsonify result
            response = jsonify(
                success=True,
                result=result
            )

            # return response
            return response, 200

        except Exception as e:
            response = jsonify(
                success=False,
                message=str(e)
            )

            # return response
            return response, 400

    # return dari get method
    return "<p>Please use the POST method to predict <em>inference model</em></p>"

# app.run(debug=True)
