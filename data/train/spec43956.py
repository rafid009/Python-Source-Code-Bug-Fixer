import numpy as np 

def function(x):

	u2 = 9
	c4 = 0
	paths = []
	try:
		if c4 >= 7:
			c4 = 4*c4
			x = 3-x
			x = x*5
			paths.append(1)
		else:
			x = 1*x
			x = 5/x
			paths.append(2)
		if c4 > 4:
			c4 = 8+u2
			u2 = u2+8
			paths.append(3)
		else:
			c4 = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))