import requests
from weather_forecasting import wether_forecast , from_json_to_readalble_forecast



def weather_forecast_to_question_animal(weather , grasses , animals):
    """Function to convert the weather forecast to a question for the GPT-3 model with all the information needed"""
    text = f'''
Types of Available Grasses: {grasses}

Nutritional Requirements of the Animals: {animals}

Weather Forecasts: 
{from_json_to_readalble_forecast(weather)}

analyze the weather forecast and check if I can feed the animals in this weather

'''
    return text


#print(weather_forecast_to_question(wether_forecast(35.6897, 51.3890) , 'Clover' , 'Cows'))