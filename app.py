from flask import Flask, render_template, request, redirect, url_for, flash , send_from_directory
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from openai_analyze import openai_function

from animal_func import weather_forecast_to_question_animal
from crop_func import weather_forecast_to_question_crop

from weather_forecasting import wether_forecast

from creatTablePDF import make_pdf_table

app = Flask(__name__)


@app.route('/api/v1/animals_check', methods=['GET'])
def animals():
    request_json = request.get_json()
    
    res = openai_function(weather_forecast_to_question_animal(wether_forecast(request_json['latitude'], request_json['longitude']) , request_json['grasses'] , request_json['animals']))
    return {
        'msg':res
        }



@app.route('/api/v1/crops_check', methods=['GET'])
def crop():
    request_json = request.get_json()
    qus = weather_forecast_to_question_crop(wether_forecast(request_json['latitude'], request_json['longitude']) , request_json['soil_quality'] , request_json['crop_rotation'] , request_json['irrigation_type'] , request_json['water_retention'] , request_json['crop_type'])
    res = openai_function(qus)
    print(qus)
    return {
        'msg':res
        }

@app.route('/api/v1/download_weather_forecast', methods=['POST'])
def download_weather_forecast():
    lat = request.form.get('lat')
    lon = request.form.get('long')
    make_pdf_table(wether_forecast(lat, lon))
    return send_from_directory(directory='.', path='weather_forecasting.pdf',filename='weather_forecasting.pdf')



@app.route('/index', methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['long']
        soil_quality = request.form.get('soil_quality')
        crop_rotation = request.form.get('crop_rotation')
        irrigation_type = request.form.get('irrigation_type')
        water_retention = request.form.get('water_retention')
        crop_type = request.form.get('crop_type')
        res = openai_function(weather_forecast_to_question_crop(wether_forecast(lat, lon) , soil_quality , crop_rotation , irrigation_type , water_retention , crop_type))
        return render_template('home.html' , res=res)
    else:
        return render_template('home.html' , res='Results !')






if __name__ == '__main__':
    app.run(debug=True , port=5005)