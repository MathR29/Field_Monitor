from soil import *
from field import *
from crops import *

milho = Corn(12)
solo = Soil("mandioca")
talhao_1 = Field("Ouro Verde","Talhao 1",50,milho,"2024-05-10","mandioca")
talhao_1.create_speadsheet()
print(talhao_1)

print(milho)
print(solo)
