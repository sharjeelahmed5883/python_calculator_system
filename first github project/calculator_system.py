
import math
from fractions import Fraction

num1 = float(input("enter a number: "))
operator = input("enter operator(+ , - , * , / , log10 , ln , frac): ")

if operator == "log10":
    if num1 <= 0:
        print("syntax error ! log can not use negative numbers")
    else:
        print(f"log10({num1}) = {math.log10(num1)}")
elif operator == "ln":
    if num1 <= 0:
        print("math error ! natural log only positive values")
    else:
        print(f"ln({num1}) = {math.log(num1)}")
elif operator == "frac":
    print(f"Fraction form of {num1} is = {Fraction(num1).limit_denominator()}")
elif operator in ("+", "-", "*", "/"):
    num2 = float(input("enter a second number: "))
    if operator == "+":
        print("Result =", num1 + num2)
    elif operator == "-":
        print("Result =", num1 - num2)
    elif operator == "*":
        print("Result =", num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            ans = num1 / num2
            print("Decimal Result =", ans)
            print("Fraction Result =", Fraction(ans).limit_denominator())
else:
    print("Invalid Operator!")
