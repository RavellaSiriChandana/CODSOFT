a=float(input("Enter value of a: "))
op=input("Enter Operator(+,-,/,%,*): ")
b=float(input("Enter value of b: "))
if op == "+":
    print("Result: ",a+b)
elif op == "-":
    print("Result: ",a-b)
elif op == "/":
    if b!=0:
        print("Result: ",a/b)
    else:
        print("Not Possible")    
elif op == "%":
    print("Result: ",a%b) 
elif op == "*":
    print("Result: ",a*b)           