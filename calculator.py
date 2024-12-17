def take_input():
    num1 = int(input("Enter first number:"))
    num2= int(input("Enter second number:"))
    choice = int(input("Which operation to be performed \n 1.Add \n 2.Subtraction \n 3.Multiplication \n 4. Division \n 5. Modulus"))
    match choice:
        case 1: return addition(num1,num2)
        case 2 : return subtraction(num1,num2)
        case 3 : return multiplication(num1,num2)
        case 4 : return division(num1,num2)
        case 5 : return modulus(num1,num2)
        case _ : return print("You have choosed a wrong option!!")

    

def addition(num1,num2):
    ans = num1+num2
    print("Ans is ",ans)

def subtraction(num1,num2):
    ans = num1-num2
    print("Ans is ",ans)

def division(num1,num2):
    if num2!=0:
        ans = num1/num2
    else:
        ans = num2/num1
    print("Ans is ",ans)

def multiplication(num1,num2):
    ans = num1*num2
    print("Ans is ",ans)

def modulus(num1,num2):
    ans = num1%num2
    print("Ans is ",ans)

take_input()