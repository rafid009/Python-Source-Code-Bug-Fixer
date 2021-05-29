import numpy as np 

def function(x):

	g6 = x
	x5 = 4
	paths = []
	try:
		if g6 < 3:
			x5 = x5*x
			x5 = x5/6
			paths.append(1)
		else:
			g6 = 1+g6
			x5 = x5-1
			paths.append(2)
		if x5 < 0:
			x = x*8
			x = x+3
			x = x-x5
			paths.append(3)
		else:
			g6 = g6/x
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