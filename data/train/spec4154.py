import numpy as np 

def function(x):

	c9 = x
	j4 = x
	paths = []
	try:
		if j4 <= 7:
			c9 = x-x
			paths.append(1)
		else:
			j4 = j4*j4
			paths.append(2)
		if x < 3:
			x = x-x
			x = 6+j4
			paths.append(3)
		else:
			j4 = 1*3
			x = x+x
			c9 = c9-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))