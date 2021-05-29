import numpy as np 

def function(x):

	u5 = x
	c8 = 4
	paths = []
	try:
		if c8 < 3:
			c8 = c8*9
			c8 = c8+4
			x = x+x
			paths.append(1)
		else:
			x = 8*x
			u5 = 2-u5
			paths.append(2)
		if c8 >= 4:
			u5 = u5+c8
			u5 = 6*8
			c8 = 3-5
			paths.append(3)
		else:
			c8 = 2+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))