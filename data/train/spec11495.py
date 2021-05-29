import numpy as np 

def function(x):

	z3 = x
	c8 = 5
	paths = []
	try:
		if c8 < 3:
			x = c8-x
			paths.append(1)
		else:
			c8 = 9+c8
			x = c8/7
			paths.append(2)
		if x > 6:
			c8 = z3/c8
			c8 = c8/c8
			x = c8-c8
			paths.append(3)
		else:
			x = 9*z3
			c8 = z3/c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))