import numpy as np 

def function(x):

	c9 = 7
	y3 = x
	paths = []
	try:
		if c9 > 5:
			c9 = c9/2
			c9 = c9-4
			paths.append(1)
		else:
			y3 = 5/x
			c9 = c9*0
			c9 = 7/6
			paths.append(2)
		if x >= 3:
			y3 = 1*y3
			x = x/8
			c9 = c9/y3
			paths.append(3)
		else:
			c9 = 3*c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))