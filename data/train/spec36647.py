import numpy as np 

def function(x):

	n5 = 8
	g0 = 7
	paths = []
	try:
		if x <= 2:
			x = x-7
			paths.append(1)
		else:
			g0 = 1/9
			n5 = x/n5
			g0 = g0/4
			paths.append(2)
		if n5 <= 1:
			x = 3-1
			g0 = g0-9
			paths.append(3)
		else:
			g0 = 1-g0
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