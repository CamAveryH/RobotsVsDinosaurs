 #* Assigns values such as health and how fighting will work to the dinosaur class, to be pulled into the Herd class

class Dinosaurs:
    
    def __init__(self, name, attack_damage):
        self.name = name
        self.health = 50
        self.attack_damage = attack_damage
    
    def attack(self, robot):
        robot.health -= self.attack_damage