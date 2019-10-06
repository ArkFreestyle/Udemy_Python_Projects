"""Simple calculator implementation with python following a udemy course"""
import re

print("Our magical calculator!")
print("Type quit to exit\n")

result = 0
run = True


def perform_math():

    global run
    global result
    if result == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(result))

    if equation == "quit":
        print("Goodbye you freak")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        # If this is the first time then result is 0 and we
        # only evaluate the given equation
        if result == 0:
            result = eval(equation)
        # After the first time, we evaluate the new equation
        # with the previous result
        else:
            result = eval(str(result) + equation)


while run:
    perform_math()
    x = 3*52 + 5*3
