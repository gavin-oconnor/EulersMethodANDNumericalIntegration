from math import sin, cos, tan, atan, asin, acos, sinh, cosh, tanh, log, log10
import math
import ast

e = math.e
pi = math.pi

def eulersMethod(givenX, givenY, steps, approxValue,func):
    step = (approxValue-givenX)/(steps-1)
    y = givenY
    x = givenX
    for i in range(steps-1):
        slope = eval(func)
        x += step
        y = y + slope*(step)
    return y

def integrateNumerically(a,b,func,steps):
    deltaX = (b-a)/steps
    sum = 0
    while a < b:
        x = a
        sum += eval(func) * deltaX
        a += deltaX
    return sum


def eulers():
    print("-----------------------------------------------------------")
    print("Welcome to the Euluer's Method Differential Equation Solver")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    print("This solver allows you to input the derivative of a function")
    print("and a point on the curve of that function to approximate values\nof that function without knowing the original function\nThe user also sets a certain amount of steps for the solver to use \nwhich changes how accurate the found approximation is\nMake sure to use * for multiplication\nMake sure to use ** instead of ^ for exponents")
    print("-----------------------------------------------------------")

    while True:
        function = input("dy/dx = ")
        originalPt = input("Point on y(x), in format (x,y): ")
        value = float(eval(input("What value of y(x) are you approximating: ")))
        steps = int(input("Steps: "))
        originalPt = ast.literal_eval(originalPt)
        print()
        x = float(originalPt[0])
        y = float(originalPt[1])
        print(f"y({value}) ≈ {round(eulersMethod(x,y,steps,value,function),5)}")
        print("\n\n\n")

def integrate():
    print("-----------------------------------------------------------")
    print("Welcome to the Numerical Integration Calculator")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    print("This solver allows you to give a function and an upper\nand lower bound, then solver will then find the area under the curve in that region")
    print("-----------------------------------------------------------")

    while True:
        function = input("y = ")
        bounds = input("Upper and lower bounds in the form (a,b): ")
        steps = float(eval(input("How many steps would you like to use (more steps, more accurate approximation): ")))
        bounds = ast.literal_eval(bounds)
        print()
        a = float(bounds[0])
        b = float(bounds[1])
        if b < a:
            a,b = b,a
        print(f"The area under y = {function} is approximately {round(integrateNumerically(a,b,function,steps),5)}")
        print("\n\n\n")

print("-----------------------------------------------------------")

if input("Would you like to use the Euler's Method Differential Equation Solver (Press E, then return)\nOr would you like to the Numerical Integration Tool (Press N, then return): ") == "E":
    eulers()
else:
    integrate()






