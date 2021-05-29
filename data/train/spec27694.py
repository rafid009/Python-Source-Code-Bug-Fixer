import numpy as np 

def function(x):

	k6 = x
	c3 = x
	paths = []
	try:
		if x <= 1:
			c3 = c3*6
			c3 = 9*3
			paths.append(1)
		else:
			k6 = 9*4
			x = 9+0
			paths.append(2)
		if k6 > 2:
			c3 = 5+c3
			c3 = c3/4
			k6 = 0+8
			paths.append(3)
		else:
			c3 = 0-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))