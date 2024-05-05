#Taking the two numbers as input.
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

#Now,we will write functon of addition
def Addition():
    add=num1+num2
    print("Addition of two number is:",add)

#Now,we will write functon of subtraction
def Subtraction():
    sub=num1-num2
    print("Subtraction of two number is:",sub)

#Now,we will write functon of multiplication
def Multiplication():
    product=num1*num2
    print("Multiplication of two number is:",product)

#Now,we will write functon of division
def Divison():
    div=num1/num2
    print("Division of two number is:",div)

#Now,we will write functon to find the remainder
def Remainder():
    mod=num1%num2
    print("Remainder is:",mod)


"""For example,we want to do addition of two number.
Then call the addition function and perform the operation."""

Addition()


"""For example,we want to do addition of two number.
Then call the subtraction function and perform the operation."""

Subtraction()


"""For example,we want to do addition of two number.
Then call the multiplication function and perform the operation."""

Multiplication()


"""For example,we want to do addition of two number.
Then call the division function and perform the operation."""

Divison()


"""For example,we want to find the remainder.
Then call the remainder function and perform the operation."""

Remainder()




