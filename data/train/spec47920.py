import numpy as np 

def function(x):

	o6 = 4
	c0 = x
	paths = []
	try:
		if c0 >= 6:
			x = x-8
			paths.append(1)
		else:
			o6 = o6+x
			o6 = o6/o6
			paths.append(2)
		if c0 >= 4:
			x = 3+x
			x = x+0
			c0 = x/x
			paths.append(3)
		else:
			c0 = c0-9
			o6 = o6*4
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))