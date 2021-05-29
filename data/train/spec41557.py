import numpy as np 

def function(x):

	e3 = 6
	g7 = x
	paths = []
	try:
		if e3 < 5:
			e3 = e3+6
			g7 = e3-7
			paths.append(1)
		else:
			e3 = 9/g7
			x = x*g7
			e3 = 7*e3
			paths.append(2)
		if x >= 8:
			e3 = e3/e3
			x = e3-x
			x = g7/x
			paths.append(3)
		else:
			e3 = e3-e3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))