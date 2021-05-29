import numpy as np 

def function(x):

	c3 = x
	i4 = 6
	x = x
	paths = []
	try:
		if x >= 3:
			c3 = 4+i4
			x = x+6
			paths.append(1)
		else:
			c3 = c3-7
			c3 = c3-4
			i4 = 1-i4
			paths.append(2)
		if i4 > 6:
			c3 = 6/c3
			i4 = i4*0
			paths.append(3)
		else:
			i4 = 4+i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))