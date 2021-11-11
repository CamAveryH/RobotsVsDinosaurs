from dinosaurs import Dinosaurs

class Herd:
    def __init__(self):
        self.dino_list = []
    
    def create_herd(self):
        dino_1 = Dinosaurs("DreadTooth", 45)
        dino_2 = Dinosaurs("TitanoSaurus", 25)
        dino_3 = Dinosaurs("MoraleRaptor", 30)
        self.dino_list.append(dino_1)
        self.dino_list.append(dino_2)
        self.dino_list.append(dino_3)
        