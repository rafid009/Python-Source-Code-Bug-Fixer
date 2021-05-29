import numpy as np 

def function(x):

	u7 = x
	c8 = x
	paths = []
	try:
		if c8 > 4:
			c8 = 0+c8
			c8 = c8*3
			u7 = 8/c8
			paths.append(1)
		else:
			c8 = u7-0
			c8 = u7/8
			paths.append(2)
		if x >= 4:
			x = x*9
			paths.append(3)
		else:
			x = x/5
			x = x-c8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))