#if-else statements:
#======================

import turtle

#create a pencil to draw:
pencil = turtle.Turtle()
pencil.speed(2)

#steps to draw square:
def square():
    pencil.forward(100)
    pencil.right(90)
    pencil.forward(100)
    pencil.right(90)
    pencil.forward(100)
    pencil.right(90)
    pencil.forward(100)

#steps to draw traingle:
def triangle():
    pencil.forward(100)
    pencil.right(120)
    pencil.forward(100)
    pencil.right(120)
    pencil.forward(100)

###########################################################################################################
    
# Now, change the values of below variables to decide what gets drawn:
A = 5
B = 15

if (A>B):
    square()
    print("And that's a Square:)")
elif (A<B):
    triangle()
    print("And that's a Triangle:)")
else:
    square()
    triangle()
    print("Ah!! I couldn't decide so I drew both the square and triangle, but somehow it looks like a B:)")

############################################################################################################