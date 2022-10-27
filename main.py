import random
# SCope:
#       global And local Scope
#       local Scope from If,while,for are available
#     local scope from Funtion is not available outside the scope of the function


# Below is example of local scope variable inside a funtion

# Below is global varibale
# which wont be accessible inside function
# Below is example

 # number=5
 # def increase():
 #     number=number+1
 #     print(number)
 #
 # print(number)
 # increase()

 #  Now we have possible two solutions
 # 1
 # First Create a global varibale inside the function
# number=5
# def increase():
#     # Below we are creating global variable
#     global number
#     number=number+1
#     print(number)
#
# print(number)
# increase()


# 2
# We simply retrun value
# number=5
# def increase():
#     # we are returning number variable and adding a number with it
#     # while we cant take its reference and add something to it but can return a value
#     return number+1
#
# print(number)
# number=increase()
# print(number)

#  Main Project
# Guessing Game



# 1Ask User to chose level of Game
difficulty_level=input("Enter Your Difficulty level Easy or Hard ")
number_of_lifes=0
if difficulty_level=="Easy":
    number_of_lifes=10
elif difficulty_level=="Hard":
    number_of_lifes=5
Mystery_Number=random.randint(1,100)


if difficulty_level=="Easy":
   while True:
     if number_of_lifes>1:
        guess_number=int(input("Enter A Number"))
        if guess_number>Mystery_Number:
            print("To High")
            number_of_lifes=number_of_lifes-1
        elif guess_number<Mystery_Number:
            print("To Low ")
            number_of_lifes=number_of_lifes-1
        else:
            print(f"Correct the mystery Number was {Mystery_Number}")
            number_of_lifes=number_of_lifes-1
            break

     elif number_of_lifes<=1:
         print("You are out of lives")
         break

if difficulty_level=="Hard":
   while True:
     if number_of_lifes>1:
        guess_number=int(input("Enter A Number"))
        if guess_number>Mystery_Number:
            print("To High")
            number_of_lifes=number_of_lifes-1
        elif guess_number<Mystery_Number:
            print("To Low ")
            number_of_lifes=number_of_lifes-1
        elif guess_number==Mystery_Number:
            print(f"Correct the mystery Number was {Mystery_Number}")
            number_of_lifes=number_of_lifes-1

     elif number_of_lifes<= 1:
         print("You are out of lives")
         break