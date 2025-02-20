from SerVivo import SerVivo
from Animal import Animal
from Planta import Planta
from Fungo import Fungo

capivara = SerVivo("Capivara", "Animale")
cavalo =  Animal("Cavalo","Animalia", "terrestre")
mangueira = Planta("Mangueira", "Plantae", "C3")
shiitake = Fungo("Shiitake", "Fungi", "assexuada")

print(capivara.exibirInfo())
print(cavalo.exibirInfo())
print(mangueira.exibirInfo())
print(shiitake.exibirInfo())