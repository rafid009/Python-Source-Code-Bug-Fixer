import numpy as np 

def function(x):

	c6 = x
	u3 = x
	paths = []
	try:
		if x < 3:
			x = 4+u3
			u3 = 8-c6
			paths.append(1)
		else:
			c6 = 9*x
			x = x-9
			paths.append(2)
		if c6 < 9:
			c6 = c6-5
			paths.append(3)
		else:
			c6 = 2+c6
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