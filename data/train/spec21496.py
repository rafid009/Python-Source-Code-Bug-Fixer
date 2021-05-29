import numpy as np 

def function(x):

	c5 = 0
	k6 = 7
	paths = []
	try:
		if k6 >= 1:
			k6 = k6-x
			c5 = 3*k6
			k6 = 7*x
			paths.append(1)
		else:
			x = c5*7
			c5 = 9/k6
			x = 6*8
			paths.append(2)
		if c5 < 7:
			k6 = k6/k6
			paths.append(3)
		else:
			x = x*6
			k6 = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))