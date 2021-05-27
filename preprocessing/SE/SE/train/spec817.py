import numpy as np 

def function(x):

	g9 = 3
	e7 = x
	paths = []
	try:
		if e7 <= 8:
			g9 = 3-g9
			g9 = x-g9
			g9 = 6/g9
			paths.append(1)
		else:
			e7 = e7+6
			x = 4*x
			paths.append(2)
		if g9 > 1:
			x = x/x
			e7 = e7+6
			e7 = 0*e7
			paths.append(3)
		else:
			e7 = e7*x
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