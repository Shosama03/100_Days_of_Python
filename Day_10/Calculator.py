from os import system
from art import logo

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "Invalid inputs for Division"
    

calculations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
    
}

def calculator():
    print(logo)
    should_accumulate= True
    num1=float(input("What is the first number?: "))

    while should_accumulate:
        
        for symbol in calculations:
            print(symbol)
        operation_symbol=input("Pick an operation: ")   
        num2=float(input("What is the second numbner?: "))
        answer = calculations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation." )

        if choice == "y":
            num1=answer
        else:
            should_accumulate = False
            system("cls")
            calculator()
            
calculator()
