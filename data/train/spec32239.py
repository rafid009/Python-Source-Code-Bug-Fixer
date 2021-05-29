import numpy as np 

def function(x):

	c6 = 0
	n1 = x
	paths = []
	try:
		if c6 < 3:
			n1 = n1-x
			c6 = 8*1
			paths.append(1)
		else:
			c6 = c6/2
			paths.append(2)
		if c6 < 9:
			n1 = c6*1
			x = x+x
			c6 = 8*c6
			paths.append(3)
		else:
			n1 = n1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))