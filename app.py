# Server script for deployment with Flask web framework

#Import the necessary libraries
from flask import Flask, jsonify, request
from flask import render_template
import xgboost as xgb
import pandas as pd
import pickle
from helper_functions import DataPreprocessingXGB, DataPreprocessingRFG


#Initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder='template')

#create our "home" route using the "index.html" page
@app.route('/')
def home():
    return render_template('index.html')


#Set a post method to yield predictions on  page
@app.route('/api', methods = ['POST'])
def predict():
    #load input data
    data_dict = {}
    for key, val in request.form.items():
        if key == "select_model":
            pass
        else:
            data_dict[key] = val
    df = pd.DataFrame([data_dict])

    model_type = request.form.get('select_model')

    #Load XGB model
    xgb_model = xgb.XGBRegressor()
    xgb_model.load_model("xgb_model22.bin")

    #Load RFG model
    with open('rfg_model22.pkl','rb') as file:
        rfg_model=pickle.load(file)

    if model_type=="rfg":
        try:
            preprocessed_df = DataPreprocessingRFG(df)
        except:
            return jsonify("Error occurred while preprocessing your data for our model!")
        predictions= rfg_model.predict(preprocessed_df)
        rsquare = 0.87

    else:
        try:
            preprocessed_df = DataPreprocessingXGB(df)
        except:
            return jsonify("Error occurred while preprocessing your data for our model!")
        predictions= xgb_model.predict(preprocessed_df)
        rsquare = 0.90

    #Round the output to 2 decimal places
    output = round(predictions[0], 2)
    return render_template('index.html', prediction_text = 'Predicted Price of the house is: ${:.2f} and R-square score of trained model being {:.2f}'.format(output, rsquare)) #r2_score


if __name__=='__main__':
    #app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


