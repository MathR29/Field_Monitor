from soil import *
from field import *
from crops import *
from weather import *
import os
import pandas as pd

import weather

class Farm: 

    def __init__(self,field,soil,weather,crop):
        self.farm_name: str = field.farm
        self.field = field.output()
        self.soil = soil.output()
        self.weather = weather.df_weather
        self.crop = crop.output()

    def create_spreadsheets(self):
        path = f"Propriedades/{self.farm_name.replace(" ","_")}/{self.field["Talhao"][0].replace(" ","_")}"
        try:
            os.makedirs(path,
                        exist_ok= True)

        except:
            print(f"An error occurred trying to create `{path}`! ")
        
        dictionary = self.field | self.crop | self.soil
        df = pd.DataFrame(dictionary)
        df.to_csv(path_or_buf = f"{path}/info.csv",
                  index=False)
        self.weather.to_csv(path_or_buf = f"{path}/weather.csv")
        return None
 




