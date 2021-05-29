import numpy as np 

def function(x):

	g0 = x
	i4 = x
	paths = []
	try:
		if g0 > 2:
			g0 = 8+g0
			paths.append(1)
		else:
			x = 3/g0
			paths.append(2)
		if i4 <= 8:
			x = g0+x
			paths.append(3)
		else:
			g0 = g0+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))