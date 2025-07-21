class Field:
    
    def __init__(self,farm,field_name,area,cultivar,planting_date,observations):
        self.farm = farm
        self.field_name = field_name
        self.area = area
        self.cultivar = cultivar
        self.planting_date = planting_date
        self.observations = observations

    def output(self):
        output_data = {
            "Fazenda": [self.farm],
            "Talhao": [self.field_name],
             "Area": [self.area],
            "Cultivar": [self.cultivar],
            "Data_de_Plantio": [self.planting_date],
            "Obs": [self.observations]
        }
        return output_data



