import numpy as np 

def function(x):

	c8 = x
	n4 = 4
	paths = []
	try:
		if c8 >= 6:
			n4 = n4*7
			c8 = 5/n4
			paths.append(1)
		else:
			n4 = n4*6
			paths.append(2)
		if n4 < 0:
			n4 = 0/c8
			paths.append(3)
		else:
			n4 = 6+1
			n4 = 5/c8
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