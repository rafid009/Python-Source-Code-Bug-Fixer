import numpy as np 

def function(x):

	c4 = x
	o2 = 7
	paths = []
	try:
		if c4 >= 6:
			x = x*o2
			paths.append(1)
		else:
			o2 = c4*o2
			x = 3+4
			paths.append(2)
		if x < 3:
			c4 = c4*x
			c4 = 2-2
			paths.append(3)
		else:
			o2 = 1/2
			o2 = 6+o2
			c4 = 8+c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))