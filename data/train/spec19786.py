import numpy as np 

def function(x):

	w7 = 0
	g4 = x
	paths = []
	try:
		if w7 >= 9:
			x = x*4
			paths.append(1)
		else:
			g4 = w7-g4
			paths.append(2)
		if w7 >= 7:
			w7 = w7*w7
			g4 = g4-w7
			paths.append(3)
		else:
			w7 = w7/g4
			g4 = 1*g4
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