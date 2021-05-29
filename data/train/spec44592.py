import numpy as np 

def function(x):

	f8 = 5
	c6 = 2
	paths = []
	try:
		if c6 <= 9:
			f8 = f8+x
			f8 = f8-1
			paths.append(1)
		else:
			c6 = c6*2
			paths.append(2)
		if x >= 1:
			x = c6*f8
			c6 = 2-f8
			paths.append(3)
		else:
			c6 = 8-c6
			c6 = 7-c6
			c6 = c6/6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))