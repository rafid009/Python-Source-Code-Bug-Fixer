import numpy as np 

def function(x):

	o3 = x
	c4 = x
	paths = []
	try:
		if o3 >= 6:
			c4 = c4+2
			c4 = 9-c4
			paths.append(1)
		else:
			c4 = 7/c4
			paths.append(2)
		if o3 <= 0:
			x = 9*2
			x = 7*x
			paths.append(3)
		else:
			o3 = o3+9
			o3 = o3-5
			c4 = x+5
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		c4 = o3**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))