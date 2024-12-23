#1
a= int(input("Enter a number: "))
if a > 1000:
    print(a-(10/100)*a)
elif a > 500:
    print(a-(5/100)*a)
else:
    print("Invalid amount.")
    
    
#2
a= input("Enter if you want (Vegetarian/Non-vegetarian): ")
if a == 'Vegetarian':
    choice= input("Choose between (Salad/Pasta)")
elif a == 'Non-vegitarian':
    choice2= input("Choose between (Chicken/Fish)")
else:
    print("Invalid")        



#3
sal= int(input("Enter a employee salary: "))
if sal > 50000:
    print("High Earner.")
elif sal >= 20000:
    print("Mid Earner.")
else:
    print("Low Earner.")


#4
a= int(input('Enter a number: '))
if a % 2 == 0:
    if a % 5 == 0:
        print(f"{a} is divisible by 2 and 5.")
else:
    print("Invalid number.")


#5
marks= int(input("Enter marks: "))
if marks > 50:
    if a > 90:
        print("Excellent.")
    elif marks > 51 and a < 90:
        print("Good")
else:
    print("Fail")  
    
#6
a= int(input("Enter first number: "))  
b= int(input("Enter second number: ")) 
c= int(input("Enter third number: "))
if a > b:
    if a > c:
        print(f"{a} is the lardest number.")
elif b > a:
    if b > c:
        print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number:")            
                                         

#7
print("Welcome to the Forest Adventure")
path= input("Enter a path (left/right): ")
if path == 'left':
    choice= input("Choose between (explore/rest): ")
    if choice == 'explore':
        print("You found treasure!")
    elif choice == 'rest':
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice.") 
elif path == 'right':
    print("You fell into a trap. Game Over.")
else:
    print("Invalid path.")
    
                       
#8
print("Welcome to the Jungle Survival Challenge")
choice1= input("Do you want to (search for food/build a shelter)") 
if choice1 == 'search for food':
    choice2= input("Do you want to (hunt/gather): ")
    if choice2 == 'hunt':
        print("You were attacked by a wild animal. Game Over.")
    elif choice2 == 'gather':
        print("You found enough food. You Win!")
    else:
        print("Invalid choice.")  
elif choice1 == 'build a shelter':
    print("Your shelter collapsed in the rain. Game Over.")                                                        
else:
    print("Invalid choice.") 


#9
print("Welcome to the Space Adeventure")
choice1= input("Do you want to (land on Mars/fly to Jupiter)") 
if choice1 == 'land on Mars':
    choice2= input("Do you want to (explore/build a base): ")
    if choice2 == 'explore':
        print("You found an alien artifact. You Win!")
    elif choice2 == 'build a base':
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice.")  
elif choice1 == 'fly to jupiter':
    print("Your spaceship crashed. Game Over.")                                                        
else:
    print("Invalid choice.") 



#10
print("Welcome to the Haunted Castle.")
choice1= input("Choose between (enter a castle/run away): ")
if choice1 == 'enter a castle':
    choice2= input("Choose color of door (red/green/black): ")
    if choice2 == 'red':
        print("You entered a room full of flames. Game Over.")
    elif choice2 == 'green':
        print("You found the treasure. You Win!")
    elif choice2 == 'black':
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == 'run away':
    print("You escaped safely.")
else:
    print("Invalid choice.")


#11
print("Welcome to the Underwater World.")
choice1= input("Choose between (dive deeper/surface): ")
if choice1 == 'dive deeper':
    choice2= input("Choose color of door (search for pearls/chase the fish): ")
    if choice2 == 'search for pearls':
        print("You found a rare pearl. You Win!")
    elif choice2 == 'chase the fish':
        print("You lost underwater. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == 'surface':
    print("You returned safely.")
else:
    print("Invalid choice.")


#12
print("Welcome to the Pirate Ship Adventure.")
choice1= input("Choose between (enter a search for treasure/battle enemy ships): ")
if choice1 == 'search for treasure':
    choice2= input("Choose between (dig on the island/explore the cave): ")
    if choice2 == 'dig on the island':
        print("You found a hidden treasure chest. You Win!")
    elif choice2 == 'explore the cave':
        print("You were traped inside. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == 'battle enemy ships':
    choice3= input("Choose between (attack/defend): ")
    if choice3 == 'attack':
        print("You won the battle. You Win!")
    elif choice3 == 'defend':
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice")        
else:
    print("Invalid choice.") 
  
  
     
#13
print("Welcome to the Wizarding World")
choice1= input("Choose between (spells/potions): ")
if choice1 == 'spells':
    choice2= input("Choose between (practice magic/compete in duels): ")
    if choice2 == 'practice magic':
        print("You mastered a powerful spell. You Win!")
    elif choice2 == 'compete':
        print("You lost ta a rival wizard. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == 'potions':
    choice3= input("Choose between (brew an elixir/create posion): ")
    if choice3 == 'brew a elixir':
        print("You healed a village. You Win!")
    elif choice3 == 'create posion':
        print("Your posion backfired. Game Over.")
    else:
        print("Invalid choice")        
else:
    print("Invalid choice.") 
    



#14
print("Welcome to the Cybersecurity Mission.")
choice1= input("Choose between (track the hacker/secure the system): ")
if choice1 == 'track the hacker':
    choice2= input("Choose between (track their IP/decode thier message): ")
    if choice2 == 'track their IP':
        print("You caught the hacker. You Win!")
    elif choice2 == 'decode their message':
        print("The message was trap. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == 'secure the system':
    choice3= input("Choose between (shut down the server/upgrade the firewall): ")
    if choice3 == 'shut down the server':
        print("Teh attack was stooped. You Win!")
    elif choice3 == 'upgrade the firewall':
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice")        
else:
    print("Invalid choice.")
 
 
    
#15
a= int(input("Enter a number: "))
if a % 2 == 0 and a % 7 == 0:
    print("Double Seven")
elif a % 2 == 0:
    print("Even")
elif a % 7 == 0:
    print("Lucky Seven")
else:
    print(a)        


#16
a= int(input("Enter a number: "))
if a > 100:
    print("Big Number.")
elif a > 50 and a < 100:
    print("Medium Number")
else:
    print("Small Number") 


#17
a= input("Enter a color (Red/Yellow/Green): ")
if a == 'Red':
    print("Stop")
elif a == 'Yellow':
    print("Slow down")
elif a == 'Green':
    print("Go")
else:
    print("Invalid signal")            



#18
a= int(input("Enter temp in celsius: "))
if a > 40:
    print("Hot")
elif a > 20 and a < 39:
    print("Warm")
else:
    print("Cold") 


#19
BMI= float(input("Enter a weight: "))
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 24.9:
    print("Normal weight")
elif BMI >= 25 and BMI < 29.9:
    print("Overweight")
else:
    print("Obesity")             
    
    

#20
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))  
if a % 2 == 0 and b % 2 == 0:
    print(a+b)
elif a % 2 == 0 or b % 2 == 0:
    print(a-b)
else:
    print(a*b)


#21
a= int(input("Enter a number: "))
if a > 1000:
    print(a-(20/100)*a)
elif a > 500 and a < 1000:
    print(a-(10/100)*a)
else:
    print("No discount")        


#22
a= int(input("Enter your age: "))
gender= input("Enter your gender (M/F): ")
income= int(input("Enter your income: "))
if a >= 18 and a < 60:
    if gender == 'M':
        if income > 1000000:
             print("Tax= 30%") 
        elif income < 1000000 and income > 500000:
            print("Tax= 20%")
        else:
            print("Tax= 10%")
    elif gender == 'F':
        if income > 1000000:
            print("Tax= 25%")
        elif income < 1000000 and income > 500000:
            print("Tax= 15%")
        else:
            print("Tax= 5%")
elif a >= 60:
    if gender == 'M' or gender == 'F':
        if income > 1000000:
            print("Tax= 20%")
        else:
            print("Tax= 10%")
else:
    print("Invalid age")



#23
a= int(input("Enter your age: "))
gender= input("Enter your gender (M/F): ")
score= int("Enter your academin score out of 100: ")
if a >= 18 and a <= 25:
    if gender == 'M':
        if score >= 85:
            print("Full Scholorship")
        elif score >= 70:
            print("Partial Schlorship")    
        else:
            print("No Scholorship")
    elif gender == 'F':
        if score >= 80:
            print("Full Scholorship")
        elif score >= 65:
            print("Partial Schlorship")    
        else:
            print("No Scholorship")    
else:
    print("Invaild")    



#24
a= int(input("Enter your age: "))
gender= input("Enter your gender (M/F): ")
exp= int("Enter your experience in years: ")
if a >= 21 and a <= 35:
    if gender == 'M':
        if exp >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == 'F':
        if exp >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
elif a > 35:
    if gender == 'M' or gender == 'F': 
        print("Manager Role")
    else:
        print("Invalid age")    
else:
    print("Invaild age")                                   


#25
a= int(input("Enter your age: "))
gender= input("Enter your gender (M/F): ")
stype= int(input("Choose between (Matinee/Evening): "))
if a < 12:
    if gender == 'M' or gender == 'F':
        if stype == 'Matinee':
             print("Ticket= Rs500") 
        elif stype =='Evening':
            print("Ticket= Rs700")
        else:
            print("Error")    
elif a >= 12 and a < 60:
    if gender == 'M':
        if stype == 'Matinee':
            print("Ticket= Rs800")
        elif stype == 'Evening':
            print("Ticket= Rs100")
        else:
            print("Error")
    elif gender == 'F':
        if stype == 'Matniee':
                print("Ticket= Rs700")
        elif stype == 'Evining':
            print("Ticket= Rs900")
        else:
            print("Error") 
elif a >= 60:
    if gender == 'M' or gender == 'F':
        print("Ticket= Rs600")
    else:
        print("Error")                           
else:
    print("Invalid")
                                                                   

#26
a= int(input("Enter your age: "))
gender= input("Enter your gender (M/F): ")
mtype= int(input("Choose between (Monthly/Yearly): "))
if a >= 18 and a < 30:
    if gender == 'M':
        if mtype == 'Monthly':
             print("Rs50") 
        elif mtype == 'Yearly':
            print("Rs500")
        else:
            print("Error")    
    elif gender == 'F':
        if mtype == 'Monthly':
            print("Rs60")
        elif mtype == 'Yearly':
            print("Rs600")
        else:
            print("Error")
elif a >= 30 and a <= 50:
    if gender == 'M' or gender == 'F':
        if mtype == 'Monthly':
            print("Rs60")
        elif mtype == 'Yearly':
            print("Rs600")
        else:
            print("Error")
elif a > 50:
    if gender == 'M' or gender == 'F':
        if mtype == 'Monthly':
            print("Rs40")
        elif mtype == 'Yearly':
            print("Rs400")
        else:
            print("Error")                
else:
    print("Invalid")
                                                                              