import numpy as np 

def function(x):

	f9 = 9
	g6 = 5
	paths = []
	try:
		if g6 < 3:
			x = 4*x
			paths.append(1)
		else:
			g6 = 9*g6
			g6 = 8+g6
			x = g6/x
			paths.append(2)
		if f9 < 8:
			x = 2*8
			paths.append(3)
		else:
			g6 = g6*g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))