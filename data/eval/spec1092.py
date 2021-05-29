import numpy as np 

def function(x):

	d8 = x
	c4 = x
	paths = []
	try:
		if d8 <= 9:
			x = x/6
			x = x/5
			paths.append(1)
		else:
			d8 = d8/9
			c4 = c4/d8
			c4 = c4/3
			paths.append(2)
		if d8 > 0:
			c4 = c4+c4
			d8 = d8*5
			c4 = c4-6
			paths.append(3)
		else:
			c4 = c4-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))