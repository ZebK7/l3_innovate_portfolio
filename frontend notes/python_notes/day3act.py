def yourinput():
    num = input("Please input a number. \n")
    try:
        print(f"Success! {int(num)} has been converted into an integer.")
    except:
        print("Try again.")
        yourinput()
        
yourinput()
