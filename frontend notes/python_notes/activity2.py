#activity 2
#program to print a to z using for loop

def main():
		for i in range(97,123):
			print(chr(i), end=" ")
main()
#alternative way
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

for i in alpha:
	print(i)
user_num = int(input("Choose and number between 0 and 25\n"))

print(alpha[user_num], "is what your number represents in the alphabet")
