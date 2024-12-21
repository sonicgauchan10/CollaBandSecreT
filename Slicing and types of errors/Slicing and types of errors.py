#1
a= int(input("Enter a number:"))
b= int(input("Enter another number:"))
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")   
    
#2
a= int(input("Enter a number:"))
if a % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd:")    

#3
a= int(input("Enter a number(1-12):"))
if a == 1:
    print("Janauary")
elif a == 2:
    print("February")  
elif a == 3:
    print("March") 
elif a == 4:
    print("April")
elif a == 5:
   print("May") 
elif a == 6:
    print("June") 
elif a == 7:
    print("July") 
elif a == 8:
    print("August") 
elif a == 9:
    print("September") 
elif a == 10:
    print("October") 
elif a == 11:
    print("November") 
elif a == 12:
    print("December") 
else:
    print("Error")    

#4 
a= int(input("Enter your marks:"))
if a > 80:
    print("Grade A")
elif a > 60 and a <= 80:
    print("Grade B")
elif a > 50 and a <= 60:
    print("Grade C")
elif a > 45 and a <= 50:
    print("Grade D")
elif a > 25 and a <= 45:
    print("Grade E")
else:
    print("Grade F")                        
 
#5
a= int(input('Enter a number:'))
if a % 7 == 0:
    print(f"{a} is divisible by 7.")
else:
    print(f"{a} is not divisible by 7.")    

#6
a= int(input('Enter one number:'))
b= int(input('Enter another number:'))
x= input('Enter a operator:')
if x == '+':
    print(a+b)
elif x == '-':
    print(a-b)
else:
    print("Error")        

#7
a= int(input("Enter a number:"))
if a % 5 == 0:
    print("Hello")
else:
    print("Bye") 

#8
a= int(input('Enter a number: '))
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else:    
    print(a)                
     
#9
char= input("Enter a charater: ")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("Vowel")
else:
    print("Consonant")   
    
    
    
    
     

#10
a= int(input("Enter your marks:"))
if a > 90:
    print("Grade A")
elif a >= 80 and a <= 89:
    print("Grade B")
elif a >= 79 and a <= 70:
    print("Grade C")
else:    
    print("Fail")                        
 
#11
a= int(input("Enter your age:"))
if a > 19:
    print("Adult")
elif a <= 19 and a <= 13:
    print("Teenager")
else:
    print("Child")   
         
#12
a= int(input("Enter a character: "))









#13
a = input("Enter a color: ")
if a == 'Red':
    print("Stop")
elif a == 'Yellow':
    print("Get Ready")
else:
    print("Go")    
   
#14
a= int(input("Enter your experience years: "))
b= int(input("Enter your age: "))
if a >= 2 and b > 18:
    print("Eligible")
else:
    print("Not Eligible")    
     
#15
a= int(input("Enter a temperature: "))
if a > 30:
    print("Its hot, stay hydrated!")
elif a > 15 and a < 30:
    print("Enjoy the weather!")
else:
    print("Its cold, wear warm clothes!") 
           
#16









#17
a= int(input("Enter a height: "))
if a >= 6:
    print("Selected")
else:
    print("Not Selected")    

#18
a= int(input("Enter a age: "))
if a >= 18:
    print("Allowed")
else:
    print("Not allowed")    

#19
a= input("Enter your username: ")
b= input("Enter your password: ")
if a == 'admin' and b == 'password123':
    print("Access Granted")
else:
    print("Access Denied")    

#20
a= int(input("Enter a number(1-12):"))
if a == 1 or a == 12 or a == 2:
    print("Winter")
elif a == 3 or a == 4 or a == 5:
    print("Spring")
elif a == 6 or a == 7 or a == 8:
    print("Summer")
else:
    print("Autumn")        

#21
a= int(input("Enter your salary: "))
b= int(input("Enter your credit score: "))
if a >= 50000 and b >= 700:
    print("Eligible")
else:
    print("Not Eligible") 
       
#22
a= int(input("Enter a number: "))
if a > 1 and a < 100:
    print("Number is valid.")
else:
    print("Number is invalid.")             