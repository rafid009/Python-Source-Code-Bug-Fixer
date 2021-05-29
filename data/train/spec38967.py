import numpy as np 

def function(x):

	x8 = x
	c7 = 9
	paths = []
	try:
		if x8 < 5:
			c7 = 5-x8
			paths.append(1)
		else:
			x8 = x8+4
			c7 = c7+2
			paths.append(2)
		if c7 < 7:
			x8 = x8-3
			c7 = 5/8
			c7 = c7*4
			paths.append(3)
		else:
			x8 = 0*9
			c7 = x/6
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))