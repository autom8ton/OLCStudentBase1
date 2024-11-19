#password program
##password="dog"
#userinput= input("what is the password? ")
#if userinput==password:
 #   print("access granted")
#else:
#    print("incorrect")
##############
#grading
#score=int(input("what is your score  "))
#if score>= 75:
   # print("A1")
#elif score >= 70:
 #   print("A2")
#elif score >= 65:
 #   print("B3")
#elif score >= 60:
#    print("B4")
#elif score >= 55:
#    print("C5")
#elif score >= 50:
#    print("C6")
#elif score>=45
#    print ("D7")
#elif score >=40:
#    print("E8")
#else:
#    print("you suck, F9")
####################
###task
#buy=int(input("how many pen are you going to buy? "))
#if buy>= 100:
 #   print("you will recieve a 10% discount")
#else:
 ##   print("you will not recieve a discount")
#cost= buy*5
#if buy>= 100:
 #   cost*0.9
#else:
#   #  None
# #print("you total price is",cost)
# ####################################
# #######number game
# import random
# print("lets play a game. guess the number")
# for i in range(7):
    
#     rannum = random.randint(1,100) 
#     guess= int(input("what is your guess? "))
#     if guess>rannum:
#         print("your guess is too big")
#     elif guess<rannum:
#         print("your guess is too small")
    
#     else:
#         print("you are correct")
#         break
# else:
#     print("all chances are used up. the answer is", rannum)
#################
# anim1=input("enter an animal ")
# anim2=input("enter an animal ")
# anim3=input("enter an animal ")
# if anim1 =="monkey" or anim2=="monkey" or anim3=="monkey":
#     print("go bananas ")
# else:
#     print("thats is a boring zoo ")
# while True:
#     topping=input("what topping do you want ")
#     if topping=="exit":
#         print("OK sending in order ")
#         break
# else:
#     print("ok , added",topping)

#######################
#riddle
# while True:
#     riddle=input("what is a dear with no eyes? ")

#     if riddle =="no idea":
#         print("correct!")
#         break
#     else:
#        print("youre wrong ")

# while True:
#     riddle2= input("what is something that people use more than you but you own it? ")
#     if riddle2 == "my name" :
#         print("you are correct")
#         break
#     else:
#         print("you are wrong try again")
0
# while True:
#     otp =input("what is your otp")
#     if len(otp) !=4:
#         print("otp must be 4 digits, try again")
#     else:
#         print("otp accepted")
#         break

'''
Question 3 (Range Check):
Write the input entry and validation code for a program 
that needs to accept a secondary student's age.

The age must be between 13 and 16 inclusive.

If the input is invalid, your code should keep trying 
by asking for the input to be entered again.

Sample output:
Enter age: 12
Invalid input. Age must be between 13 and 16.
Enter age: 20
Invalid input. Age must be between 13 and 16.
Enter age: 16
Age accepted.
'''
# while True:
#     age=int(input("what is your age"))
#     if age <13:
#         print("invalid age")
#     elif age>16:
#         print("invald age")
#     else:
#         print("thank you")
#         break
##############
# while True:
#     user=str(input("what is your username "))
#     if user.isupper():
#         print("invalid username try again with no caps")
#     else:
#         print("thaank you")
#         break
bags_rice = 10
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")