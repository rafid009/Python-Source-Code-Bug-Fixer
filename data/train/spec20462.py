import numpy as np 

def function(x):

	c0 = 7
	n6 = 3
	paths = []
	try:
		if x <= 5:
			c0 = c0-c0
			x = 1/x
			paths.append(1)
		else:
			n6 = 1*n6
			n6 = n6*8
			paths.append(2)
		if x > 7:
			x = x/n6
			c0 = 9+4
			n6 = x*7
			paths.append(3)
		else:
			n6 = n6*4
			x = 0-x
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