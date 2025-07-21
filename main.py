import farm
import field


talhao1 = field.Field("Ouro Verde","Talhao do Milho",31,"Milho","2012-10-10","Milho Verao")
fazenda1 = farm.Farm(talhao1,"","","")

fazenda1.create_spreadsheets()
