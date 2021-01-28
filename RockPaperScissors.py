#Getting all of the libraries I need
import random


from time import sleep


#Making a list of all the choies the computer has
List = ["Rock", "Paper", "Scissors"]



#Starting a loop so that my code can rerun         
while True:
    #assigning a variable to the computers random choice
    x = random.choice(List)
    
    #Letting the computer ask a
    user = input("What would you like to play, r = rock, p = paper, s = scissors, and e = exit:")
    #Giving every Possible situation that can happen 
    if user == "r" and x == "Paper":
        print("I played paper, and you played rock, YOU LOSE")
            
        
    elif user == "p" and x == "Rock":
        print("I played Rock, and you played Paper, YOU WIN")
          
          
          
    elif user == "s" and x == "Paper":
        print("I played Paper, and you played Scissors, YOU WIN")
           
           
           
    elif user == "r" and x == "Scissors":
        print("I played Scissors, and you played Rock, YOU WIN")
              
              
              
    elif user == "s" and x == "Rock":
        print("I played Rock, and you played Scissors, YOU LOSE")
                
                
                
    elif user == "p" and x == "Scissors":
        print("I played Scissors, and you played paper, YOU LOSE")
                
                
                
    #Now Listing every situation where it can be a tie
    elif user == "p" and x == "Paper":
        print("Its A draw")
               
               
               
    elif user == "r" and x == "Rock":
        print("Its A draw")
                
                
                
    elif user == "s" and x == "Scissors":
        print("Its A draw")
        
        
        
    #Giving an exit feature in case you want to exit the code
    elif user == "e":
        print("Thank You for playing!!")
        break
    
    
    
    #Just in case they give and input that isn't valid
    else:
        print("This is not a valid option")
   
   
   #adding a sleep so whoever is running the code has time to read the answer
    sleep(2)
        
    
        
