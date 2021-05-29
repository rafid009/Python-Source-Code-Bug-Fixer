import numpy as np 

def function(x):

	c4 = x
	r0 = x
	paths = []
	try:
		if x >= 9:
			r0 = c4/x
			c4 = 7-7
			paths.append(1)
		else:
			r0 = x*r0
			r0 = r0+6
			paths.append(2)
		if x <= 1:
			x = 5-x
			paths.append(3)
		else:
			c4 = 0*c4
			c4 = 8*3
			r0 = 5-x
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