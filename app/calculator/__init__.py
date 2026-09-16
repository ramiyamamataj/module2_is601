from app.operations import addition, subtraction, multiplication, division

def calculator():
    print("Welcome to the calculator REPL")
    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break
        
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input format. Usage: <operation> <num1> <num2>")
                continue
                
            op, num1_str, num2_str = parts
            num1 = float(num1_str)
            num2 = float(num2_str)
            
            if op == "add":
                res = addition(num1, num2)
            elif op == "subtract":
                res = subtraction(num1, num2)
            elif op == "multiply":
                res = multiplication(num1, num2)
            elif op == "divide":
                res = division(num1, num2)
            else:
                print("Invalid operation.")
                continue
                
            print(f"Result: {res}")
        except ValueError as e:
            print(f"Invalid input: {e}")