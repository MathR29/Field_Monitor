import os

print("Field Monitor")

class Field:
    def __init__(self,farm,field_name,area,current_crop,planting_date):
        self.farm = farm
        self.field_name = field_name
        self.area = area
        self.current_crop = current_crop
        self.planting_date = planting_date
        try:
            os.makedirs(f"Farms/{self.farm.replace(' ','_')}/{self.field_name.replace(' ','_')}")
        except:
            pass


Talhao_1 = Field("Fazenda Ouro Verde","Talhao 1",25,"Milho","2023-25-01")
Talhao_2 = Field("Fazenda Ouro Verde","Talhao 2",30,"Soja","2023-23-01")
