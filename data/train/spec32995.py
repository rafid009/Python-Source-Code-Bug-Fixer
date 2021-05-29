import numpy as np 

def function(x):

	x5 = x
	g4 = x
	paths = []
	try:
		if g4 >= 5:
			x = x+0
			paths.append(1)
		else:
			x = g4*x
			paths.append(2)
		if g4 > 9:
			x5 = 9*x5
			x = 4-x
			g4 = 2*g4
			paths.append(3)
		else:
			x5 = x5/2
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))