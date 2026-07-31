# This is a comment

bill = 0

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    print("Small Pizza(S): $15")
    bill = int(15)
elif size == "M":
    print("Medium Pizza(M): $20")
    bill = int(20)
elif size == "L":
    print("Large Pizza(L): $25")
    bill = int(25)
else:
    print("Please choose the correct size!")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    print("Pepperoni: $3")
    bill = int(bill + int(3))
else:
    print("It's Ok, Thanks!")

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    print("Extra Cheese: $2")
    bill = int(bill + int(2))
else:
    print("It's Ok, Thanks!")

print(f"You needs to pay ${bill}")
