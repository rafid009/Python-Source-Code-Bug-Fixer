import numpy as np 

def function(x):

	g4 = 4
	b7 = x
	paths = []
	try:
		if b7 >= 0:
			g4 = g4/g4
			g4 = g4-g4
			paths.append(1)
		else:
			g4 = 6+3
			b7 = 4+b7
			paths.append(2)
		if g4 >= 1:
			g4 = x-g4
			paths.append(3)
		else:
			x = x*b7
			b7 = b7+5
			x = b7/x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))