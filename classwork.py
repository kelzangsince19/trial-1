#eligibilty for cost discount
user = input("are you a student? (yes/no :)")
age = int(input("enter your age :"))
if age <= 12 :
    print("you are elligible for discount")
elif age <= 12 and user == "yes":
    print("you are elligible for ticlek discount!:")
elif age <= 18 and user == "yes":
    print("you are elligible for ticlek discount!:")    
else:
    print("sorry, you are not elligible for ticket discount")        



