import numpy as np 

def function(x):

	g7 = 6
	e5 = x
	paths = []
	try:
		if g7 >= 6:
			g7 = g7/x
			g7 = 9/2
			paths.append(1)
		else:
			x = x+3
			g7 = e5*e5
			paths.append(2)
		if g7 < 0:
			e5 = 8+e5
			x = 2-4
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))