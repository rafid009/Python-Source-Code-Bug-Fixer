import numpy as np 

def function(x):

	c1 = 2
	x3 = 8
	paths = []
	try:
		if x3 > 0:
			c1 = c1*7
			c1 = 1-c1
			c1 = x*2
			paths.append(1)
		else:
			c1 = c1/4
			x3 = x3+x3
			c1 = c1/4
			paths.append(2)
		if c1 >= 6:
			x3 = x3/9
			c1 = 9/x3
			c1 = c1-8
			paths.append(3)
		else:
			x3 = 0+4
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