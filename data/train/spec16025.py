import numpy as np 

def function(x):

	c2 = 0
	n5 = 8
	paths = []
	try:
		if x > 3:
			x = 4/1
			n5 = 0*n5
			paths.append(1)
		else:
			n5 = n5-1
			paths.append(2)
		if c2 >= 2:
			c2 = x-c2
			paths.append(3)
		else:
			c2 = c2/8
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