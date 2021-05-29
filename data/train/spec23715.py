import numpy as np 

def function(x):

	r9 = 6
	c6 = 2
	x = x
	paths = []
	try:
		if c6 > 8:
			c6 = 3*x
			paths.append(1)
		else:
			r9 = r9/6
			c6 = 3+x
			paths.append(2)
		if c6 <= 9:
			r9 = 3-r9
			r9 = 4-0
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))