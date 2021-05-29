import numpy as np 

def function(x):

	b9 = 3
	c3 = 7
	paths = []
	try:
		if c3 > 8:
			x = 3/3
			c3 = b9+c3
			b9 = x*b9
			paths.append(1)
		else:
			c3 = 1+c3
			paths.append(2)
		if x < 1:
			b9 = 5/b9
			paths.append(3)
		else:
			b9 = 4+2
			x = c3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))