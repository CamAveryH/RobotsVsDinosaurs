from robot import Robots

#* Creates a list of Robots and their defined stats which will be imported into the Battlefield class
class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()
    
    def create_fleet(self):
        robot_1 = Robots("D34th-B0t 4000")
        robot_2 = Robots("Sh1eld-B0t 2230")
        robot_3 = Robots("R3pa1r Dr01d 17")
        self.robot_list.append(robot_1)
        self.robot_list.append(robot_2)
        self.robot_list.append(robot_3)