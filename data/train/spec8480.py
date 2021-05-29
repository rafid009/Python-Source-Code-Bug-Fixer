import numpy as np 

def function(x):

	c6 = 3
	o0 = x
	paths = []
	try:
		if c6 < 7:
			c6 = c6*o0
			x = x-x
			paths.append(1)
		else:
			o0 = o0+6
			c6 = c6/c6
			o0 = 4-o0
			paths.append(2)
		if c6 <= 7:
			x = 6+5
			c6 = x*o0
			paths.append(3)
		else:
			c6 = c6-7
			o0 = c6+x
			o0 = o0*5
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		c6 = o0**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))