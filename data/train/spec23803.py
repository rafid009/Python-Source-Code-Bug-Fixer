import numpy as np 

def function(x):

	g3 = x
	c7 = 2
	paths = []
	try:
		if c7 < 0:
			x = x*g3
			g3 = 0/g3
			c7 = c7/9
			paths.append(1)
		else:
			g3 = 4-g3
			x = c7/x
			x = 8+x
			paths.append(2)
		if x >= 8:
			c7 = c7*g3
			x = 5-c7
			paths.append(3)
		else:
			c7 = c7/2
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		c7 = g3**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))