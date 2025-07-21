from PyNasaPower.NasaPower_request import get_power

#df = get_power(
#    period = "daily",
#    parameters = ["T2M","PRECTOTCORR"],
#    community = "AG",
#    latitude = -24,
#    longitude = 24,
#    start = "2024-01-01",
#    end = "2024-12-01"
#)
#
#print(df)

class Weather:
    df_weather = None 
    def __init__(self,lat,long,start_date,end_date):
        self.df_weather = get_power(
            period = "daily",
            parameters = ["T2M","T2M_MAX","T2M_MIN","PRECTOTCORR"],
            community = "AG",
            latitude = lat,
            longitude = long,
            start = start_date,
            end = end_date
        )
