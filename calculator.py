def add(n1, n2):
        return n1+n2

def sub(n1, n2):
        return n1-n2

def mul(n1, n2):
        return n1*n2

def div(n1, n2):
        return n1/n2

def calculator():
    num1 = float(input("Enter first number: "))
    while True:    
        op_dict = {"+":add,"-":sub,"*":mul,"/":div}
        for symbol in op_dict:
            print(symbol)
        operation = input("Select an operation: ")
        num2 = float(input("Enter second number: "))

        result = op_dict[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        continue_with_result = input(f"Type 'yes' to continue calculating with {result} " \
        "or 'no' to start a new calculation. ").lower()

        if continue_with_result=="no":
            print("\n" * 20)
            calculator()
        elif continue_with_result=="yes":
            num1=result
              
calculator()
          
    
