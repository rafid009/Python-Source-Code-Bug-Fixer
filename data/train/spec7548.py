import numpy as np 

def function(x):

	e0 = x
	g9 = 0
	x = x
	paths = []
	try:
		if x < 5:
			e0 = 0+e0
			g9 = g9+6
			paths.append(1)
		else:
			e0 = 6-x
			paths.append(2)
		if g9 < 6:
			x = x-e0
			x = g9+2
			x = 9+6
			paths.append(3)
		else:
			g9 = 5*6
			g9 = g9*g9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))