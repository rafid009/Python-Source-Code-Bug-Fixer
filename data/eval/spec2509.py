import numpy as np 

def function(x):

	c1 = 0
	u2 = 3
	paths = []
	try:
		if c1 >= 7:
			x = 5*x
			paths.append(1)
		else:
			u2 = 5-u2
			x = 0/5
			u2 = 4+u2
			paths.append(2)
		if c1 > 7:
			x = 4-x
			c1 = x-u2
			u2 = u2/u2
			paths.append(3)
		else:
			u2 = 4-8
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))