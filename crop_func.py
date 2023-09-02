import requests
from weather_forecasting import wether_forecast , from_json_to_readalble_forecast




def weather_forecast_to_question_crop(weather , Soil_Quality , Crop_Rotation:int , irrigation_type , water_retention:int , crop):
    """Function to convert the weather forecast to a question for the GPT-3 model with all the information needed"""
    text = f'''
Analyze and check if I can grow the crop

Crop: {crop} Find specific requirements for growing this crop.

Soil Quality: {Soil_Quality}

Crop Rotation: {Crop_Rotation} days

Irrigation Type: {irrigation_type}

Water Retention: {water_retention} days

Weather Forecasts: 
{from_json_to_readalble_forecast(weather)}

'''
    return text


# print(weather_forecast_to_question_crop(wether_forecast_crop(73.03671526236255, -40.04956496442478) , 'Clay' , 2 , 'Drip' , 3 , 'Wheat'))
# print(weather_forecast_to_question(wether_forecast(35.6897, 51.3890) , 'Clay' , 2 , 'Drip' , 3))
