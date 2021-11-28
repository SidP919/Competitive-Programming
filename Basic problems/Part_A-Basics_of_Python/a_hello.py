#Say hello to the world of python:
msg = "Hello World of Python"
print(msg)


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

###############################################################################################


# Datatypes in python:
# ====================
# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview


# Operators in python:
# ====================
#
# Arithmetic:
# -----------
# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	
# %	    Modulus	        x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	
#
# Logical:
# --------
# and 	    Returns True if both statements are true	               Ex: x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	           Ex: x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	   Ex: not(x < 5 and x < 10)
