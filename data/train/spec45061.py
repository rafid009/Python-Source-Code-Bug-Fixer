import numpy as np 

def function(x):

	c8 = 4
	u9 = x
	x = 5
	paths = []
	try:
		if c8 <= 8:
			x = 5*x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x <= 8:
			x = 4*6
			paths.append(3)
		else:
			x = 9-7
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		c8 = u9**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))