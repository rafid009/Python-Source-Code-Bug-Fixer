import numpy as np 

def function(x):

	g6 = 6
	p0 = x
	paths = []
	try:
		if g6 >= 7:
			x = x-g6
			paths.append(1)
		else:
			g6 = g6-x
			p0 = 5-p0
			paths.append(2)
		if x < 1:
			x = x+g6
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		g6 = p0**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))