import numpy as np 

def function(x):

	e3 = 2
	g0 = 6
	paths = []
	try:
		if x < 4:
			e3 = e3*7
			e3 = e3+6
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if g0 > 4:
			g0 = g0+e3
			x = e3*x
			paths.append(3)
		else:
			g0 = 6-8
			e3 = 8+e3
			x = g0-0
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