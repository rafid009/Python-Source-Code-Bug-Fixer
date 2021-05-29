import numpy as np 

def function(x):

	c3 = x
	c6 = x
	paths = []
	try:
		if c6 < 5:
			x = x*5
			paths.append(1)
		else:
			x = 4/x
			c3 = x+6
			c6 = 9/c6
			paths.append(2)
		if c3 >= 7:
			c6 = 4*1
			paths.append(3)
		else:
			c3 = c3*1
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c3 = c6**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))