from dinosaurs import Dinosaurs

class Herd:
    def __init__(self):
        self.dino_list = []
        self.create_herd()

    
    def create_herd(self):
        dino_1 = Dinosaurs("DreadTooth", 45)
        self.dino_list.append(dino_1)
        dino_2 = Dinosaurs("TitanoSaurus", 25)
        self.dino_list.append(dino_2)
        dino_3 = Dinosaurs("MoraleRaptor", 30)
        self.dino_list.append(dino_3)
        