# Agri-Bot API


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
