import numpy as np 

def function(x):

	c5 = 0
	f7 = 3
	paths = []
	try:
		if x <= 1:
			f7 = 5+9
			paths.append(1)
		else:
			f7 = f7*7
			x = x+6
			x = 4-x
			paths.append(2)
		if x > 8:
			f7 = f7/f7
			paths.append(3)
		else:
			c5 = c5-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))