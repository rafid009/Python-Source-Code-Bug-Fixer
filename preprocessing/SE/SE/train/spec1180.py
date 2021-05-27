import numpy as np 

def function(x):

	c0 = 3
	u1 = x
	paths = []
	try:
		if c0 <= 6:
			x = c0/x
			x = 7*x
			c0 = c0*c0
			paths.append(1)
		else:
			c0 = c0/8
			paths.append(2)
		if x >= 9:
			c0 = 3-c0
			u1 = u1*3
			x = x-3
			paths.append(3)
		else:
			c0 = c0-2
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		u1 = c0**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))