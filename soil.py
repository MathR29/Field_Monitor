import pandas as pd 

class Soil:
    def __init__(self,field_id):
        df = pd.read_csv("Soil_Analysis.csv").query("plot_id == @field_id")
        self.P = df["p"].values[0]
        self.K = df["k"].values[0]
        self.Ca = df["ca"].values[0]
        self.Mg = df["mg"].values[0]
        self.clay = df["clay"].values[0]
        self.ctc = df["ctc"].values[0]
        
    def output(self):
        output_data = {
            "P_solo": [self.P],
            "K_solo": [self.K],
            "Ca_solo": [self.Ca],
            "Mg_solo": [self.Mg],
            "Argila": [self.clay],
            "CTC": [self.ctc]
        }
        return output_data


