from soil import *
from field import *
from crops import *
from weather import *
import os

class Farm: 

    def __init__(self,field,soil,weather,crop):
        self.farm_name: str = field.farm
        self.field = field
        self.soil = soil
        self.weather = weather
        self.crop = crop

    def create_spreadsheets(self):
        path = f"Propriedades/{self.farm_name.replace(" ","_")}/{self.field.field_name.replace(" ","_")}"
        try:
            os.makedirs(path,
                        exist_ok= True)

        except:
            print(f"An error occurred trying to create `{path}`! ")



