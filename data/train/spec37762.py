import numpy as np 

def function(x):

	u1 = x
	c0 = 8
	paths = []
	try:
		if x >= 7:
			x = x-5
			c0 = u1/c0
			paths.append(1)
		else:
			x = c0+x
			x = 2-x
			paths.append(2)
		if x <= 7:
			x = 4-x
			c0 = 6/7
			c0 = x-5
			paths.append(3)
		else:
			u1 = u1*u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))