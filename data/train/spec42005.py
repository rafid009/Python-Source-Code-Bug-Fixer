import numpy as np 

def function(x):

	x3 = x
	g4 = 2
	paths = []
	try:
		if g4 > 1:
			x = x3+x
			paths.append(1)
		else:
			x = 8+0
			paths.append(2)
		if g4 >= 2:
			g4 = 5/5
			paths.append(3)
		else:
			x = x+3
			g4 = g4*6
			g4 = x3*g4
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))