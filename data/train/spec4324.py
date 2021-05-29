import numpy as np 

def function(x):

	c3 = x
	r6 = 9
	paths = []
	try:
		if r6 >= 0:
			c3 = 9-c3
			x = 9*x
			x = x+3
			paths.append(1)
		else:
			x = r6/1
			x = 0*x
			r6 = 9-r6
			paths.append(2)
		if x >= 5:
			r6 = x-7
			c3 = 9*c3
			paths.append(3)
		else:
			c3 = c3/r6
			r6 = 3/8
			c3 = 4/c3
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