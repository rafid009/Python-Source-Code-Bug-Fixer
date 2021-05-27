import numpy as np 

def function(x):

	c3 = 7
	e4 = 9
	x = x
	paths = []
	try:
		if c3 <= 3:
			x = x+8
			e4 = 3+8
			c3 = 7*8
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x > 4:
			c3 = c3*4
			c3 = c3-c3
			paths.append(3)
		else:
			e4 = 8+x
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		c3 = e4**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))