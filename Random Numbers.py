import random

#Produces a random number between 1 and 5 (Up to but not including the second number)
random.randint(1,6)

#produces a value between 0 and 5 (Up to but not including the second number)
random.randrange(6)

#Example:Range of 1-5?????? This code seems to have a range of 1-6
die1=random.randint(1,6)
print(die1)

# Example: Range of 1-6
die2=random.randrange(6)+1
print(die2)

#IF/ELSE
password=input("What is your password?")
if password=="secret":
    print("Access granted.")
else:
    print("Access denied.")

#In Python, <> means the same thing as !=.

#Doesn't do anything for values 31-100
dressPrice=input("How much did you pay for your dress?")
if int(dressPrice)>500:
    print("That's a lot of money for a dress.")
elif int(dressPrice)<30:
    print("That is cheap.")
    print("Where did you get your dress?")
elif int(dressPrice)>100:
    print("Very nice!")
    print("Is it for weekday or Shabbos?")


#While loop
studentCount=int(input("How many girls are in the class?"))
counter=1
while counter<=studentCount:
    studentName=input("What is the next student name?")
    print("Hello",studentName)
    counter=counter+1

if password=="secret" or password=="password":
    print("You have selected one of the two worst passwords")
else:
    print("What a unique password!")

