import numpy as np 

def function(x):

	c3 = x
	o3 = 0
	paths = []
	try:
		if x <= 9:
			x = 7*2
			x = x/2
			c3 = c3*x
			paths.append(1)
		else:
			x = x/x
			x = x*3
			paths.append(2)
		if x < 3:
			x = x-x
			x = x+2
			paths.append(3)
		else:
			c3 = 0*x
			o3 = c3-2
			c3 = c3*3
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		c3 = o3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))