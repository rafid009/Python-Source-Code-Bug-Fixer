import numpy as np 

def function(x):

	g1 = 0
	n5 = 2
	paths = []
	try:
		if x < 0:
			x = 3-x
			paths.append(1)
		else:
			n5 = n5/x
			n5 = 5/x
			paths.append(2)
		if x > 2:
			g1 = g1/4
			n5 = g1/x
			x = 3-x
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))