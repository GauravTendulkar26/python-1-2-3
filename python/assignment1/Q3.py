
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
print("Please select operation -\n" "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select=int(input("enter the choice 1,2,3,4:"))
num1=int(input('Enter the first Number'))
print(num1)
num2=int(input('Enter the Second Number'))
print(num2)
if select==1:
    print('Addition=',add(num1,num2))

elif select==2:
    print('sub=',sub(num1,num2))
elif select==3:
    print('multiply=',multiply(num1,num2))
elif select==4:
    print('division=',division(num1,num2))
else:
    print('Invalid input')