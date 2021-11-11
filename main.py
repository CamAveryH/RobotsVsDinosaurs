from battlefield import Battlefield

# Only for testing
from dinosaurs import Dinosaurs
from robot import Robots

robros = Robots("D34th-B0t 4000")
dino = Dinosaurs("DreadTooth", 45)


robros.attack(dino)
print(dino.name)
dino.attack(robros)
print (dino.health)
print (robros.name)
print (robros.health)