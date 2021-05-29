import numpy as np 

def function(x):

	x5 = x
	g2 = 6
	paths = []
	try:
		if x5 >= 0:
			x5 = g2*6
			paths.append(1)
		else:
			x5 = 3-g2
			paths.append(2)
		if x >= 7:
			g2 = g2/4
			x5 = x5/4
			paths.append(3)
		else:
			x5 = 2-x
			g2 = g2-0
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