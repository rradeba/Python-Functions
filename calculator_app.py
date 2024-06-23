# task 1-3
print("Welcome to calculator. I can calculate simple problems with two integers and one operator.")
num1 = int(input("What is your first number: "))
num2 = int(input("What is the second number: "))
operator = input("What is the operator (+,-,*,/): ")

def add_operator(a, b) :
    return a + b
def sub_operator(a, b) :
    return a - b
def mult_operator(a, b) :
    return a* b
def div_operator(a, b) :
    return a / b


if operator == "+" :
    print("The sum is: ", float(add_operator(num1, num2)) )
elif operator == "-" :
    print("The difference is: ", float(sub_operator(num1, num2)))
elif operator == "*" :
    print("The product is: ", float(mult_operator(num1, num2)))
elif operator == "/" :
    if  num2 == 0: 
        print("undefined")
    print("The quotient is: ", float(div_operator(num1, num2)))
else: 
    print("Please try again and type one of the recommended operators.")
