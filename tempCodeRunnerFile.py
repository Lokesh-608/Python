def calculate(a, b, operator):
    if operator == 1:
        print(a + b, end="")   
    elif operator == 2:
        print(a - b, end="")   
    elif operator == 3:
        print(a * b, end="")   
    else:
        print("Invalid Input", end="")  
        calculate(1, 2, 3) 


