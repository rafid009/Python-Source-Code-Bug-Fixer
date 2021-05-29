import numpy as np 

def function(x):

	o8 = 4
	c6 = 0
	paths = []
	try:
		if x >= 1:
			c6 = o8*c6
			o8 = 2-o8
			o8 = o8/7
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if c6 < 0:
			x = x*6
			x = x+6
			c6 = x*2
			paths.append(3)
		else:
			o8 = x-o8
			c6 = x+5
			c6 = c6-9
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		c6 = o8**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))