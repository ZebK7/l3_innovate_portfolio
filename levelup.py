# print("this is level up")
# int(5.4)
# int("54")
# print()
# print(int(5.4))
# print(type(int("54")))
# balance =100
# deposit = int(input("how much do you want to deposit"))
# balance +=deposit
# print (f" you have {balance}")

# print("whats your name")
# name = input()

# if name:
#     print(f"welcome {name} to innovate!")
# else:
#     print("you didnt enter a name")

# day="monday"
# bank_hol =""
# if day =="saturday" or day=="sunday" or bank_hol:
#     print("yay a day off")
# else:
#     print("off to work")

# allowed=["John","Paul","George","Ringo"]
# name=input("whats your name? ")

# while name not in allowed:
#     print("your names not on list")
#     print("try again")
#     name=input("whats your name? ")

#     print("come in")

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    
    try:
        print(int(num1) + int(num2))
    except:
            print("please use numbers only")
            print("try again")
            add_up()
add_up()
