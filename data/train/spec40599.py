import numpy as np 

def function(x):

	k4 = x
	c2 = 5
	paths = []
	try:
		if c2 >= 9:
			c2 = 8+c2
			paths.append(1)
		else:
			c2 = c2+c2
			k4 = k4*1
			paths.append(2)
		if c2 > 7:
			k4 = k4-c2
			paths.append(3)
		else:
			k4 = k4-c2
			k4 = k4/4
			x = c2/8
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		c2 = k4**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))