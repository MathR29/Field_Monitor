import os
import pandas as pd

print("Field Monitor")

class Field:
    def __init__(self,farm,field_name,area,current_crop,planting_date):
        self.farm = farm
        self.field_name = field_name
        self.area = area
        self.current_crop = current_crop
        self.planting_date = planting_date
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
                "Planting Date": [self.planting_date]
                }
        data = pd.DataFrame(data)
        data.to_csv((self.path+ f"/{self.field_name}.csv"),
                    index = False)


Talhao_1 = Field("Ouro Verde","Pastagem_1",124,"Marandu","2023-05-14")
Talhao_1.create_speadsheet()
