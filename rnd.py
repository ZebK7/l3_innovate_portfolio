import random

 #print(random.random())
#print(random.uniform(1,10))
#print(random.randint(1,10))

my_name="Zeb"
my_age=51
student=False

#print(my_name,my_age,student)

#print("Hello my name is", my_name)
#print("I am", my_age)
#print("Hello my name is " + my_name)
#print("I am " + my_age)

#.format method, used to be best practice using {} as placeholders and data filled in based on order of arguments
#print("Hello my name is {} and I am {} years old".format(my_name, my_age))

#print("Hello my name is {my_name} and I am (my_age) years old")
#print(1+2)
#print(3-2)
#print(3*3)
#print(3**3)
#print(5/2)
#print(16%3)

#balance=100
#amount=20

#balance=amount+balance
#print(balance)
#balance +=amount
#print(balance)

#answer=input("What is your name? \n")
#print(answer)

#music = "classical"

#if music == "classical":
#    print("Oh no its classical")
#elif music == "no music":
#    print("Put the radio on")
#else:
#    print("turn it up")

# day = "monday"
# bank_hol = True

# if day == "saturday" or day =="sunday" or bank_hol:
#     print("a day off")
# else:
#     print("off to innovate")

# def light_switch():
#     print("Switching the lights")

# light_switch()
# light_switch()

# def cash_with(amount,accnum):
#     print(f"withdrawing {amount} from {accnum}")

# cash_with(300,12345678)
# cash_with(100,123456785678)
# cash_with(1268,125486)

fav_songs = [
    "Paint it Black - Rolling Stones",
    "Break on Through - The Doors",
    "Bat out of Hell - Meatloaf"
]
print(fav_songs)
fav_songs[1] = "Ragdoll - Aerosmith"

print(fav_songs)
print(len(fav_songs))
fav_songs.append("Enter Sandman -Megadeath")
print(fav_songs)
fav_songs.pop(2)
print(fav_songs)
