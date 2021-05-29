import numpy as np 

def function(x):

	c8 = 8
	u7 = x
	paths = []
	try:
		if u7 < 4:
			x = x+u7
			c8 = c8-6
			x = x*c8
			paths.append(1)
		else:
			c8 = 7+u7
			x = 0+x
			x = u7*x
			paths.append(2)
		if c8 < 9:
			x = 1-4
			u7 = u7*3
			u7 = u7*x
			paths.append(3)
		else:
			c8 = c8*u7
			x = 0/c8
			u7 = 2/u7
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