import farm
import field
import soil
import crops
import weather


milho = crops.Corn(12)
#print(milho.output())

solo1 = soil.Soil("mandioca")
#solo1.show()

talhao1 = field.Field("Ouro Verde","Talhao do Milho",31,"Milho","2012-10-10","Milho Verao")
#print(talhao1.output())

clima = weather.Weather(lat = -25, long= -51, start_date= "2024-01-01",end_date="2024-12-31")


fazenda1 = farm.Farm(talhao1,solo1,clima,milho)
#
#
fazenda1.create_spreadsheets()
