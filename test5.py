# import uuid

# print("El UUId iiod1() es :", end="")
# print(uuid.uuid1())

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

for i in range(4):
    myTurtle.forward(20)
    myTurtle.right(90)

myWin.exitonclick()