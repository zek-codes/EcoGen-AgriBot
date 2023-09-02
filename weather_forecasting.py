import requests


def wether_forecast(latitude, longitude):
    """Function to get the weather forecast from the API"""
    url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,rain,windspeed_180m,winddirection_180m,soil_temperature_0cm,soil_moisture_0_1cm'.format(latitude, longitude)
    response = requests.get(url)
    weather = response.json()
    return weather


def from_json_to_readalble_forecast(weather):
    """Function to convert the json object to a readable text"""
    text = """"""
    for x in range(len(weather['hourly']['time'])):
        text += f"""In {weather['hourly']['time'][x]} the temperature will be {weather['hourly']['temperature_2m'][x]} and the humidity will be {weather['hourly']['relativehumidity_2m'][x]} and the wind speed will be {weather['hourly']['windspeed_180m'][x]} and the precipitation will be {weather['hourly']['precipitation'][x]} and the rain will be {weather['hourly']['rain'][x]} and the soil temperature will be {weather['hourly']['soil_temperature_0cm'][x]} and the soil moisture will be {weather['hourly']['soil_moisture_0_1cm'][x]} \n\n"""
    return text
