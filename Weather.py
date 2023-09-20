# Python program to find current 
# weather details of any city 
# using openweathermap api
# By using fastAPI

# import required modules


import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
 
import requests

app = FastAPI()

class CityRequest(BaseModel):
    city_name: str



# @app.get("/", include_in_schema=False)
# async def redirect_to_docs():
#     return APIRedirect(url="/docs")

@app.post("/get_weather")
async def get_weather(city: CityRequest):
    
	# Enter your API key here 
    api_key = "f57976a0730913e865a5c60bb99dc3d8"  
    
	# base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    


	 # complete_url variable to store 
     # complete url address 
    complete_url = base_url + f"appid={api_key}&q={city.city_name}"
    
	# get method of requests module 
	# return response object
    print(complete_url)
    response = requests.get(complete_url)
    # json method of response object
    # convert json format data into  
	# python format data 
    data = response.json()
    print("Json Data")
    print(data)

    if data["cod"] != "404":
        main_data = data["main"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        weather_desc = data["weather"][0]["description"]

        return {
            "temperature": current_temperature,
            "pressure": current_pressure,
            "humidity": current_humidity,
            "description": weather_desc,
        }
    else:
        return {"error": "City not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)