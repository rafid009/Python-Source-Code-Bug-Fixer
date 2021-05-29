import numpy as np 

def function(x):

	n9 = x
	c3 = 3
	paths = []
	try:
		if n9 <= 1:
			c3 = x/c3
			paths.append(1)
		else:
			n9 = n9+c3
			paths.append(2)
		if x < 0:
			c3 = 3*3
			paths.append(3)
		else:
			x = 2/c3
			x = x*x
			n9 = n9+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))