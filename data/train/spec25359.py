import numpy as np 

def function(x):

	c3 = x
	p2 = 3
	paths = []
	try:
		if c3 >= 6:
			c3 = 8+c3
			paths.append(1)
		else:
			x = c3-6
			c3 = c3+8
			paths.append(2)
		if x >= 0:
			c3 = 7-4
			paths.append(3)
		else:
			c3 = 5*p2
			x = 7+x
			x = p2/x
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