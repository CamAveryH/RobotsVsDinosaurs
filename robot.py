from weapons import Weapons

class Robots:
   
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.weapon = Weapons("Laser Blast", 20)
    
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_damage
        

# 1. print one of the names assigned to a robot
# 2. I think I'm calling the object incorrectly but dont remember how exactly to do it
# 3. Multiple diffrent ways of calling the object or making it print bur it hasnt worked yet.
# 4. not much, it doesn't run through any of the methods how it's coded now