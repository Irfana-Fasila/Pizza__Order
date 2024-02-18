print("Thankyou for choosing python pizza deliveries!")
size = input("what size pizza do you want?S,M,or L")
add_pepperoni =input("do you want pepperoni? Y or N")
extra_cheese = input("do you want extra cheese? Y or N")
 bill = 0
 if size =="S":
     bill+=15
 elif size =="M":
     bill+=20
 else:
    bill+=25
if