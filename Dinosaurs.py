class Dinosaurs:
    
    def __init__(self, name, attack_damage):
        self.name = name
        self.health = 200
        self.attack_damage = attack_damage
    
    def attack(self, robot):
        robot.health -= self.attack_damage