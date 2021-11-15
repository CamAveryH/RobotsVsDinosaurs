 #* defines how weapons will function once they're imported into the Robots class.
class Weapons:
    def __init__ (self, name, attack_damage):
        self.name = name
        self.attack_damage = attack_damage
        
        
    #! ideas for different weapons and utilities that I hope to add before the end of the semester.  For now these are on the back-burner
    
    # def weapon_types (self):
    #     self.name_1 = "Expandable Chain Sword"
    #     self.attack_damage_1 = 15
    #     self.name_2 = "Disposable Wrist-Mounted Missle Launcher" # can only be used once
    #     self.attack_damage_2 = 30
    #     self.name_3 = "Shoulder-Mounter Ionic Laser" # must to charge for 3 turns between uses
    #     self.attack_damage_3 = 40
    #     # self.name_4 = "Nuclear Core Self-Detonation" # Robot's last ditch effort to win the battle for their team, must cost remainder of HP
    #     # self.attack_damage_4 = "65"
        
    # # def utility_types(self):
    # #     self.utility_1 = "Titanium Armor plating"
    # #     self.use_1 = "Block 15% incoming damage"
    # #     self.utility_2 = "Holographic Barrier"
    # #     self.use_2 = "Block one instance of damage completely" # can only be used once
    # #     self.utility_3 = ""