import numpy as np 

def function(x):

	b3 = 5
	c6 = x
	paths = []
	try:
		if c6 <= 6:
			c6 = c6-0
			c6 = c6-c6
			paths.append(1)
		else:
			c6 = 3+c6
			paths.append(2)
		if c6 >= 2:
			x = 8-x
			x = 7+c6
			paths.append(3)
		else:
			x = x/8
			c6 = b3+c6
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