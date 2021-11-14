#Say hello to the world of python:
msg = "Hello World of Python"
print(msg)

msg2 = msg.capitalize()

print(msg2)

print(msg.__len__())

print(msg.isdigit())

print(msg.lower())

print(msg.split())


################################################################################################


#Having fun with python:)
import turtle

#create a square
key = turtle.Turtle()
key.speed(1)

def square():
    key.forward(100)
    key.right(90)
    key.forward(100)
    key.right(90)
    key.forward(100)
    key.right(90)
    key.forward(100)
    key.right(90)

square()


##############################################################################################

#running python program/file/script in terminal:
# for windows, move to directory/folder where file is present and run command: 
# python <file-name>
# For example: python a_hello.py
# Alternatively, we can click on the play/run button on top right corner in VSCode.