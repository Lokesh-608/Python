g = int(input("Enter marks: "))
if 90 <= g <= 100:
    print("A Grade")
elif 75 <= g <= 89:
    print("B Grade")
elif 50 <= g <= 74:
    print("C Grade")
elif g < 50:  
    print("Fail")
else:
    print("Invalid marks entered.") 