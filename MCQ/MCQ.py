#1
a=int(input("a:  "))
b=int(input("b:  "))
a,b=b,a
print("a=",a,"b=",b)

# or 
a=int(input("a:  "))
b=int(input("b:  "))
a=a^b
b=a^b
a=a^b
print("a=",a,"b=",b)

#2
print("Welcome to the Treasure Land")
choice=input("Enter the direction (right or left): ")
if choice == "right":
    print("Game Over")
elif choice == "left":
    preference=input("You want to (swim or wait): ")
    if preference == "swim":
        print("Game Over")
    else:
        choose=input("Choose the colour (red, blue, yellow): ")
        if choose == "blue" or choose == "red":
            print("Game Over")
        else:
            print("You Win")
        
else:
    print("You have entered the wrong direction.")

#4
x=int(input("enter an integer: "))
if x > 0:
    print("True")
elif x < 0:
    print("False")
else:
    print("Zero")

#5
num=int(input("enter the num: "))
if num % 2 == 0:
    print(num,"is even")
else:
    print(num,"is odd")

#6
Math=float(input("math marks: "))
Sci=float(input("science marks: "))
Phy=float(input("physics marks: "))
Chem=float(input("chemistry marks: "))
Total = Math + Sci + Phy + Chem
per = (Total/400)*100
if per >= 70 and per <= 100:
    grade="distinction"
elif per >= 60 and per < 70:
    grade="first"
elif per >= 40 and per < 60:
    grade="pass"
elif per >=0 and per < 40:
    grade="Fail"
else:
    grade="invalid"

print("Result: ")
print("Total marks is: ",Total)
print(f"percentage is: {per}%")
print(f"your grade is: {grade}")

#7
cp=int(input("enter the cost price of the bike: "))
if cp > 100000:
    tax="15%"
elif cp> 50000 and cp <= 100000:
    tax="10%"
elif cp <= 50000:
    tax="5%"
else:
    tax="invalid"

print("-----Displaying the road tax-----")
print(f"Road tax of the bike is:{tax}")

#8
Aayush=int(input("enter aayush's age: "))
Adarsha=int(input("enter adarsh's age: "))
Kapil=int(input("enter nehab's age: "))
Nehab=int(input("enter nehab's age: "))

youngest=min(Aayush,Adarsha,Kapil,Nehab)

print(f"The youngest age is: {youngest}")

#9
age1=int(input("enter aayush's age: "))
age2=int(input("enter adarsh's age: "))
age3=int(input("enter nehab's age: "))
age4=int(input("enter kapil's age: "))

oldest=max(age1,age2,age3,age4)

print(f"The oldest age is: {oldest}")

#10
grade=int(input("enter your grade: "))
if grade < 25:
    result="D"
elif grade >= 25 and grade <= 45:
    result="C"
elif grade > 45 and grade <= 50:
    result="B"
elif grade > 50 and grade <= 60:
    result="B+"
elif grade > 60 and grade <= 80:
    result="A"
else:
    result="A+"
print(f"your grade is: {result}")

#11
year=int(input("enter the time you served in the bank: "))
if year > 10:
    Bonus="10%"
elif year >= 6 and year <=10:
    Bonus="8%"
else:
    Bonus="5%"
print(f"Your bonus is: {Bonus}")

#12
days=int(input("Enter the number of days: "))
if days <= 5:
    charge = days*2
elif days <= 10:
    charge = 5*2 + (days-5)*3
elif days <=15:
    charge = 5*2 + 5*3 + (days-10)*4
else:
    charge = 5*2 + 5*3 + 5*4 + (days-15)*5

print("charge for",days,f"days of the library is: Rs {charge}")

#13
salary = float(input("enter your salary: "))
service = int(input("enter the no. of years you have worked in the company: "))

if service > 5:
    print("you are eligible for obtaining bonus")
    bonus = (5/100)*salary
    final_salary = salary + bonus
    print(f"your net bonus amt is: Rs {bonus:.2f}")
    print(f"your salary with bonus will be: Rs {final_salary:.2f}")

else:
    bonus = 0
    print("You are not eligible for bonus")
    print(f"your net bonus amt is: Rs {bonus:.2f}")
    final_salary = salary
    print(f"Your salary with no bonus will be: Rs {final_salary:.2f}")

#14
r = float(input("enter the radius of the circle: "))

area_of_circle = (22/7) * r ** 2

print(f"The area of circle with radius {r} is: {area_of_circle:.2f}")

#15
import math #used for rounding up the value.

a=int(input("no of students in 1st class: "))
b=int(input("no of students in 2nd class: "))
c=int(input("no of students in 3rd class: "))
seats_a = math.ceil(a/2)
seats_b = math.ceil(b/2)
seats_c = math.ceil(c/2)
total_seats = seats_a + seats_b + seats_c
print(f"The smallest seat needed among stds in all three classroom is: {total_seats}")

#16
apple=int(input("enter the no. of apples: "))
std=int(input("enter no of students: "))

apples_per_std = apple // std   #integer div fro apples each std gets
apples_rem = apple % std       #modulud operation for remaining apples

print(f"The number of apples a std gets is: {apples_per_std}")
print(f"The no. of apple remaining in the basket is: {apples_rem}")

#17
age=int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
    print("You will be eligible once you have reached 18 or above")

#18
city = input("enter city (Delhi, Agra, Jaipur): ")
if city == 'Delhi':
    print("Monument of",city,"is Red Fort.")
elif city == 'Agra':
    print("Monumnet of",city,"is Taj Mahal.")
elif city == 'Jaipur':
    print("Monument of",city,"is Jai Mahal.")
else:
    print("You have entered the wrong city!")

#19
a=int(input("Enter the number: "))
if a%2==0 and a%3==0:
    print(a,"is divisible by both 2 and 3")
else:
    print("It is not divisible by both")

#20


#21


#22
per=float(input("enter your percentage: "))
if per < 40:
    print("Result: Failed")
elif per >= 40 and per <= 55:
    print("Result: Fair")
elif per >=55 and per < 65:
    print("Result: Good")
else:
    print("Result: Excellent")

#23
age=int(input("enter your age: "))
gender=input("enter your gender(M or F): ")
num_days=int(input("enter the no. of days: "))
if age >= 18 and age < 30:
    if gender == "M":
        wage_day = 700
        
    elif gender == "F":
       wage_day = 750
      
    else:
        print("You have entered invalid gender!")
        exit()
elif age >= 30 and age <= 40:
    if gender == "M":
        wage_day = 800

    elif gender == "F":
        wage_day = 850
    
    else:
        print("You have entered invalid gender!")
        exit()
else:
    print("Age out of range!")
    exit()
Total_wages = wage_day * num_days

print(f"Total wages for {num_days} days is: {wage_day}")

#24
a=True
b=True
c=True
d=True
print(c)                                 #True
print(d)                                 #True
print(not a)                             #False
print(not b)                             #False
print(not c)                             #False
print(not d)                             #False
print(a and b)                           #True
print(a or b)                            #True
print(a and b or c)                      #True
print(not a or b or c)                   #True
print(not a or not b or not c)           #False
print(not(not a or not b or not c))      #True 

#25
num=int(input("enter the number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

#26
actual_username="akaayush"
actual_pass= "falcon401040"

username = input("enter your username: ")
password = input("enter the password: ")

if username == actual_username:
    if password == actual_pass:
        print("Login successful!")
    else:
        print("Incorrect password!")
        exit()
else:
    print("Incorrect username!")

#27
num1 = float(input("enter 1st num: "))
num2 = float(input("enter 2nd num: "))
if num1 > num2:
    print(num1,"is greater than",num2)
elif num2 > num1:
    print(num2,"is greater than",num1)
else:
    if num1 > 0:
        print("The numbers are positive and equal")
    elif num1 < 0:
        print("The numbers are negative and equal")
    else:
        print("The numbers are zero and equal")

#28
sub_score=int(input("enter your subject score: "))
if sub_score > 90:
    print("Congratulations!")
elif sub_score >= 50 and sub_score <= 90:
    print("Improvement is needed.")
else:
    print("I think you should retake the course.")

#29
age=int(input("Enter your age: "))
if age >= 18:

    degree=input("Enter (Yes/No) for having a degree or not: ")

    if degree == "Yes":

        work_exp=float(input("Enter your work experience: "))

        if work_exp > 3:
            print("Highly Eligible.")

        elif work_exp >= 1 and work_exp <= 3:
            print("Eligible.")

        else:
            print("Under Review.")
    else:
        print("Dont have a degree.")

else:
    print("Not Eligible.")

#30
weight=float(input("Enter the weight of package: "))
if weight < 5:
    delivery_charge = 5

elif weight >= 5 and weight <= 20:
    delivery_charge = 10
    
else:
    delivery_charge = 20

urgent= input("Do you need package in urgent? (Yes/No): ").strip().lower()

if urgent == "yes":
    delivery_charge += 5
    print(f"Cost of the {weight}kg package with urgent delivery is ${delivery_charge}")
else:
    print(f"Cost of the {weight}kg package without urgent delivery is ${delivery_charge}")

#31
income=float(input("Enter your income: "))

if income > 50000:
    credit_score=int(input("Enter your credit score: "))

    if credit_score > 700:
        print("Your loan is approved.")

    elif 600 <= credit_score <=700:
        print("Your loan is approved with higher interest rate.")

    else:
        print("Your loan is rejected because of low credit score.")

else:
    print("Your loan is rejected as your income is below 50000.")

#32
weather=input("Type of weather outside(sunny/rainy): ")
if weather == "sunny":
    print("You can go for outdoor activities like hiking or a picnic.")
elif weather == "rainy":
    user=input("Type (yes/no) if the user has raincoat or umbrella.")
    if user == "yes":
        print("You can go to nearby mall or museum.")
    else:
        print("You should stay home and watch movies.")
else:
    print("Invalid weather type.")

#33
print("Welcome to the haunted house")
choice_1 = input("You want to go (upstairs/downstairs): ")

if choice_1 == "downstairs":
    print("Game Over")

elif choice_1 == "upstairs":
    choice_2 = input("You want to (enter the room/stay outside): ") 
    if choice_2 == "Enter the room":
        print("Game Over")

    elif choice_2 == "stay outside":
        choice_3 = input("You choose between (ghost/vampire/werewolf): ")
        if choice_3 == "ghost" or choice_3 == "vampire":
            print("Game Over")

        elif choice_3 == "werewolf":
            print("You win!")
        else:
            print("Invalid choice of fantasy character.")
    else:
        print("Invalid choic of staying at a place.")
else:
    print("Invalid choice.")

#34
print("Welcome to the Jungle Adventure!")
choice_1 = input("You want to go (left/right): ")

if choice_1 == "right":
    print("Game Over")

elif choice_1 == "left":
    choice_2 = input("You want to(climb a tree/explore a cave): ")

    if choice_2 == "climb a tree":
        print("Game Over")

    elif choice_2 == "explore the cave":
        choice_3 = input("Choose among (bear/tiger/snake): ")

        if choice_3 == "bear" or choice_3=="tiger":
            print("Game over.")

        elif choice_3 == "snake":
            print("You win.")

        else:
            print("Invalid choice of animals.")
    else:
        print("Invalid choice of outdoor activity.")
else:
    print("Invalid choice of direction.")

#35
print("Welcome to the Magic Forest!")
choice_1 = input("You want to go (north/south): ")

if choice_1 == "south":
    print("Game Over")

elif choice_1 == "north":
    choice_2 = input("You want to (cross the river/follow the path): ")

    if choice_2 == "cross the river":
        print("Game Over")

    elif choice_2 == "follow the path":
        choice_3 = input("Choose among (fairy/ogre/elf): ")
        if choice_3 == "ogre" or choice_3 == "fairy":
            print("Game over.")

        elif choice_3 == "elf":
            print("You win.")

        else:
            print("Invalid choice of fantasy charcters.")
    else:
        print("Invalid choice of path.")
else:
    print("Invalid choice of direction.")

#36
print("Welcome to the Space Mission!")
choice_1 = input("You want to go (to the moon/to Mars): ")

if choice_1 == "to Mars":
    print("Game Over")

elif choice_1 == "to the moon":
    choice_2 = input("You want to (land on the surface/stay in orbit): ")

    if choice_2 == "land on the surface":
        print("Game Over")

    elif choice_2 == "stay in orbit":
        choice_3 = input("Choose between (alien/asteroid/satellite): ")
        if choice_3 == "alien" or choice_3 == "asteroid":
            print("Game over.")

        elif choice_3 == "satellite":
            print("You win.")

        else:
            print("Invalid choice of space fantasies.")
    else:
        print("Invalid choice of path.")
else:
    print("Invalid choice of planet and star.")

#37
print("Welcome to the Pirate Island!")
choice_1 = input("You want to go (left/right): ")

if choice_1 == "right":
    print("Game Over")

elif choice_1 == "left":
    choice_2 = input("You want to (dig for treasure/sail the ship): ")
    if choice_2 == "dig for treasure":
        print("Game Over")

    elif choice_2 == "sail the ship":
        choice_3 = input("Choose among (shark/pirate ship/mermaid): ")

        if choice_3 == "shark" or choice_3 == "pirate ship":
            print("Game Over.")

        elif choice_3 == "mermaid":
            print("You win.")

        else:
            print("Invalid choice of displayed characters.")
    else:
        print("Invalid choice of activity.")
else:
    print("Invalid choice of direction.")






















