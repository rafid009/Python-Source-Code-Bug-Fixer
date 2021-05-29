import numpy as np 

def function(x):

	x2 = 4
	c6 = x
	paths = []
	try:
		if x >= 3:
			x2 = 9-x2
			x = x+6
			c6 = c6-7
			paths.append(1)
		else:
			x2 = c6+x2
			x = 1+x
			paths.append(2)
		if x2 <= 8:
			c6 = 8/c6
			c6 = x2-c6
			paths.append(3)
		else:
			x = x*x
			c6 = 3+c6
			x2 = c6*2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		c6 = x2**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))