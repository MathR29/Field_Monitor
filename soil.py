import pandas as pd 

class Soil:
    def __init__(self,field_id):
        self.soil_atributes = pd.read_csv("Soil_Analysis.csv").query("plot_id == @field_id")
        self.P = self.soil_atributes["p"].values[0]
        self.K = self.soil_atributes["k"].values[0]
        self.Ca = self.soil_atributes["ca"].values[0]
        self.Mg = self.soil_atributes["mg"].values[0]
        self.clay = self.soil_atributes["clay"].values[0]
        self.ctc = self.soil_atributes["ctc"].values[0]

    def show(self):
        print(self.P)
        print(self.K)
        print(self.Ca)
        print(self.Mg)
        print(self.clay)
        print(self.ctc)
        print(self.soil_atributes)


