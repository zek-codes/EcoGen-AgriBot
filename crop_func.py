import requests


def wether_forecast_crop(latitude, longitude):
    url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,rain,windspeed_180m,winddirection_180m,soil_temperature_0cm,soil_moisture_0_1cm'.format(latitude, longitude)
    response = requests.get(url)
    weather = response.json()
    return weather


def from_json_to_readalble_forecast_crop(weather):
    text = """"""
    for x in range(len(weather['hourly']['time'])):
        text += f"""In {weather['hourly']['time'][x]} the temperature will be {weather['hourly']['temperature_2m'][x]} and the humidity will be {weather['hourly']['relativehumidity_2m'][x]} and the wind speed will be {weather['hourly']['windspeed_180m'][x]} and the precipitation will be {weather['hourly']['precipitation'][x]} and the rain will be {weather['hourly']['rain'][x]} and the soil temperature will be {weather['hourly']['soil_temperature_0cm'][x]} and the soil moisture will be {weather['hourly']['soil_moisture_0_1cm'][x]} \n\n"""
    return text

# print(from_json_to_readalble_forecast(wether_forecast(35.6897, 51.3890)))


def weather_forecast_to_question_crop(weather , Soil_Quality , Crop_Rotation:int , irrigation_type , water_retention:int , crop):
    text = f'''
Analyze and check if I can grow the crop

Crop: {crop} Find specific requirements for growing this crop.

Soil Quality: {Soil_Quality}

Crop Rotation: {Crop_Rotation} days

Irrigation Type: {irrigation_type}

Water Retention: {water_retention} days

Weather Forecasts: 
{from_json_to_readalble_forecast_crop(weather)}

'''
    return text


# print(weather_forecast_to_question_crop(wether_forecast_crop(73.03671526236255, -40.04956496442478) , 'Clay' , 2 , 'Drip' , 3 , 'Wheat'))
# print(weather_forecast_to_question(wether_forecast(35.6897, 51.3890) , 'Clay' , 2 , 'Drip' , 3))
