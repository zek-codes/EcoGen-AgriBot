# Agri-Bot 

## Program Structure:

The program is built using the Python programming language and utilizes the Flask framework to create an API.
The main file, app.py, contains the API endpoints.
Additional files include animal_func.py, crop_func.py, and weather_forecasting.py. These files contain functions related to weather forecasting, formulating queries, and providing sufficient information to the ChatGPT model for analysis and suggestions.
A .env file is required to store the OPENAI_API_KEY.
Program Purpose:
The project aims to assist farmers in making informed decisions about crop cultivation and animal husbandry by utilizing artificial intelligence and weather forecasting. Here are the key functionalities:

## Crop Cultivation:

Farmers provide details about their crops and location.
The program analyzes weather forecasts for the upcoming 7 days.
It also considers the type of crop and the data provided by the farmers.
Based on this analysis, the program provides predictions and recommendations on whether it is suitable to cultivate the specified crop.

## Animal Husbandry:

Farmers can input information about animal husbandry, such as the type of animals and location.
The program analyzes weather forecasts for the next 7 days.
It provides predictions and insights on whether it is suitable to rear animals in the given location based on the weather conditions.

## Weather Forecasting:

The program also allows users to download weather forecasts for the next 7 days.
Role of Artificial Intelligence:
Artificial intelligence, specifically ChatGPT, plays a crucial role in this project. It assists in the analysis and decision-making process by:

Processing information provided by farmers.
Analyzing weather forecasts and historical data.
Formulating queries based on user inputs.
Generating predictions and recommendations.
Providing explanations and suggestions to farmers about crop cultivation and animal husbandry.
Overall, the program leverages artificial intelligence and weather forecasting to empower farmers with data-driven insights, helping them make informed choices for their agricultural and animal husbandry activities.


### Endpoins

#### /api/v1/crops_check
##### Arguments

`latitude` Location

`longitude` Location

`crop_type` Crop Name

`soil_quality` Soil quality

`crop_rotation` Crop rotation - In days

`irrigation_type` Irrigation type

`water_retention` Water retention - In days

##### Response:
Json object

`msg` explanation message


#### /api/v1/animals_check

##### Arguments

`latitude` Location

`longitude` Location

`grasses` Grasses

`animals` Animals

##### Response:

Json object

`msg` explanation message


#### /api/v1/download_weather_forecast

##### Arguments

`latitude` Location

`longitude` Location

##### Response: PDF file that contains weather forecasting for next 7 days

