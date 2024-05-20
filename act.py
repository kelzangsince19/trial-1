age = int (input("enter ur age"))
std = input ("are you a student ?(yes/no)")
if (age <= 12 or (age>= 13 and age <= 18) and std == "yes"):
    print("you are elligible for discount on the movie ticket")
else:
    print("your are elligible for a discount on the movie ticket")
        