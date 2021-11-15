from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        
        # result_1 = self.show_dino_opponent_options()
        # result_2 = self.show_robo_opponent_options()
        # print ("selected dino is: ", self.herd.dino_list[result_1].name)
        # print("selected Robot is: ", self.fleet.robot_list[result_2].name)
        self.battle()
        # self.dino_turn(self.herd.dino_list[result_1], self.fleet.robot_list[result_2])
        # self.robot_turn(self.fleet.robot_list[result_2], self.herd.dino_list[result_1])
        self.display_winners()
    
    def display_welcome(self):
        print("Welcome to the Thunder-Dome!")
        
    def battle(self):
        # use loops here
        while( len(self.fleet.robot_list) > 0 and len(self.herd.dino_list) > 0):
            print("\n*** Master Turn:") 
            chosen_dino_index = self.show_dino_opponent_options()
            chosen_robot_index = self.show_robo_opponent_options()
            
            while(self.fleet.robot_list[chosen_robot_index].health > 0) and (self.herd.dino_list[chosen_dino_index].health >0):
                print("\nChosing defender for selected attackers")
                self.dino_turn(self.herd.dino_list[chosen_dino_index])
                print("\nChosing defender for selected attackers")
                self.robot_turn(self.fleet.robot_list[chosen_robot_index])
            # Do robo turn            
   
            # * health check of selected object and remove approp
            if self.fleet.robot_list[chosen_robot_index].health <= 0:
                self.fleet.robot_list.pop(chosen_robot_index)

            if self.herd.dino_list[chosen_dino_index].health <= 0:
                self.herd.dino_list.pop(chosen_dino_index)
                print("\n ==> Testing: ", self.herd.dino_list[chosen_dino_index].health, "\n\n")


                

    def dino_turn(self, dinosaur):
        robo_index = self.show_robo_opponent_options()
        dinosaur.attack(self.fleet.robot_list[robo_index])
       
    
    def robot_turn(self, robot):
        # Who are we going to attack? (show-dino-options)  = gives us an index
        dino_index = self.show_dino_opponent_options()
                # robot attack the returned/chosen
        robot.attack(self.herd.dino_list[dino_index])
    
    #1
    def show_dino_opponent_options(self):
        #input
        count = 0
        for dino in self.herd.dino_list:
            count+=1
            print(count,") - ", dino.name) # add a number here 1) - dino name
            
        chosen_dino = int(input("Please select a Dinosaur to fight: "))
                
        if chosen_dino > len(self.herd.dino_list):
            print("Please select a number betwwen 1 and 3")
        else:
            return (chosen_dino - 1)
    
     #2
    def show_robo_opponent_options(self):
        count = 0
        for robot in self.fleet.robot_list:
            count += 1
            print(count, ") - ", robot.name)
        chosen_robot = int(input("Please select a Robot to fight: "))
       
        if chosen_robot > len(self.fleet.robot_list):
            print("Please select a number between 1 and 3")
        else:
            return (chosen_robot -1)
    
    def display_winners(self):
        pass
        if len(self.fleet.robot_list) <= 0:
            print("Dinosaurs Have Won This Match")
        elif len(self.herd.dino_list) <= 0:
            print("Robots Have Won This Match")

    #  1. trying to run the attack method, however it reads "robot" as an integer instead of the assigned index it pulls earlier in the sequence
    #  2. it throws an error that says "Health is not an assigned value" when it is within the Robots class
    #  3. So far I've used different dot notation and tried using the variable for the index it pulls inside of the turn method.  I have also tried clicking around in the de-bugger but cant find anything relevent to why it isn't working so far.
    #  4. It runs through everything, then when it reads through the health value it throws the error at me.