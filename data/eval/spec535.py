import numpy as np 

def function(x):

	c3 = 8
	v2 = x
	paths = []
	try:
		if v2 <= 9:
			v2 = 8/v2
			c3 = 7/c3
			x = 3/x
			paths.append(1)
		else:
			x = x*7
			v2 = 6-7
			paths.append(2)
		if c3 <= 8:
			c3 = c3/v2
			paths.append(3)
		else:
			c3 = c3/x
			x = x-1
			c3 = 2-c3
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		c3 = v2**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))