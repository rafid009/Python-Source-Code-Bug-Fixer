import numpy as np 

def function(x):

	o8 = 9
	c9 = x
	paths = []
	try:
		if x < 2:
			o8 = o8*4
			paths.append(1)
		else:
			c9 = 2*c9
			c9 = 0/o8
			o8 = 6+o8
			paths.append(2)
		if x <= 4:
			o8 = 0+3
			c9 = c9-o8
			c9 = 1-o8
			paths.append(3)
		else:
			o8 = x*o8
			c9 = c9/5
			o8 = c9*o8
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