import numpy as np 

def function(x):

	o0 = x
	c5 = x
	x = 9
	paths = []
	try:
		if o0 >= 8:
			x = 5-x
			o0 = 6-o0
			paths.append(1)
		else:
			o0 = o0*6
			c5 = 9/c5
			x = c5+x
			paths.append(2)
		if c5 > 8:
			o0 = o0+o0
			c5 = 9+5
			c5 = x*x
			paths.append(3)
		else:
			x = x-x
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