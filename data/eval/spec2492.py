import numpy as np 

def function(x):

	d2 = 9
	c0 = 4
	x = x
	paths = []
	try:
		if x >= 4:
			x = c0/4
			d2 = 0/x
			paths.append(1)
		else:
			c0 = c0-6
			c0 = c0*6
			paths.append(2)
		if d2 > 0:
			x = c0-c0
			d2 = x-d2
			x = x*d2
			paths.append(3)
		else:
			d2 = d2+7
			d2 = d2/6
			c0 = 8*c0
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