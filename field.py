import os
import soil
import pandas as pd


class Field:
    def __init__(self,farm,field_name,area,current_crop,planting_date,field_id):
        self.farm = farm
        self.field_name = field_name
        self.area = area
        self.current_crop = current_crop
        self.planting_date = planting_date
        self.soil = soil.Soil(field_id)
        self.path = f"Farms/{self.farm.replace(' ','_')}/{self.field_name.replace(' ','_')}"
        try:
            os.makedirs(self.path)
        except:
            pass
    
    
    def create_speadsheet(self): 
        data = {"Farm": [self.farm],
                "Field": [self.field_name],
                "Area": [self.area],
                "Crop": [self.current_crop],
                "Planting Date": [self.planting_date],
                "Nitrogen": [self.soil.P],
                "Potassium": [self.soil.K],
                "Calcium": [self.soil.Ca],
                "Magnesium": [self.soil.Mg],
                "CTC": [self.soil.ctc],
                "Clay": [self.soil.clay]
                }
        data = pd.DataFrame(data)
        data.to_csv((self.path+ f"/{self.field_name}.csv"),
                    index = False)


