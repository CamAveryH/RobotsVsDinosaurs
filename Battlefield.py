from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    #^ Welcomes the player to the game, and begins the Battle method.  This prompts the user to select one of three options from both
    #^ Robot and Dinosaur teams, and runs a battle loop until one team is victorious, the winner is displayed in the terminal
    
    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
    
    def display_welcome(self):
        print("Welcome to the Thunder-Dome!")
        
    #! runs a loop for the remaining length of both dinosaur and robot lists. Once one list has been made empty, the loop ends and
    #! Display winner runs
    
    def battle(self):
        while( len(self.fleet.robot_list) > 0 and len(self.herd.dino_list) > 0):
            print("\n*** Master Turn:") 
            chosen_dino_index = self.show_dino_opponent_options()
            chosen_robot_index = self.show_robo_opponent_options()
            
           
           #! Checks the health of both robots and dinosaurs during the fight, once a healthbar is depleted to 0, the item is popped from
           #! the list.  This loops until either one of the selected teams has no health remaining
           
            while(self.fleet.robot_list[chosen_robot_index].health > 0) and (self.herd.dino_list[chosen_dino_index].health >0):
                print("\nChosing defender for selected attackers")
                self.dino_turn(self.herd.dino_list[chosen_dino_index])
                print("\nChosing defender for selected attackers")
                self.robot_turn(self.fleet.robot_list[chosen_robot_index])         
            
            if self.fleet.robot_list[chosen_robot_index].health <= 0:
                self.fleet.robot_list.pop(chosen_robot_index)

            if self.herd.dino_list[chosen_dino_index].health <= 0:
                self.herd.dino_list.pop(chosen_dino_index)
                print("\n ==> Testing: ", self.herd.dino_list[chosen_dino_index].health, "\n\n")
              
    #& Both dino and robot turns will run through when prompted, continuing to decrement health points for both dinosaurs and robots based on
    #& attack power
      
    def dino_turn(self, dinosaur):
        robo_index = self.show_robo_opponent_options()
        dinosaur.attack(self.fleet.robot_list[robo_index])
        
    def robot_turn(self, robot):
        dino_index = self.show_dino_opponent_options()
        robot.attack(self.herd.dino_list[dino_index])
    
    #* Presents all options for dinosaurs within the terminal and allows for user-selection
    
    def show_dino_opponent_options(self):
        count = 0
        for dino in self.herd.dino_list:
            count+=1
            print(count,") - ", dino.name) 
        
        chosen_dino = int(input("Please select a Dinosaur to fight: "))    
                
        if chosen_dino > len(self.herd.dino_list):
            print("Please select a number betwwen 1 and 3")
        else:
            return (chosen_dino - 1)
    
     #* Presents all options for robots within the terminal and allows for user selection
    
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
    
    #^ Reads through the length of the dinosaur and robot lists and determines when one list has been emptied.  No need to read health
    #^ as it is decremented to 0 during the fighting sequence
    
    def display_winners(self):
        pass
        if len(self.fleet.robot_list) <= 0:
            print("Dinosaurs Have Won This Match")
        elif len(self.herd.dino_list) <= 0:
            print("Robots Have Won This Match")
