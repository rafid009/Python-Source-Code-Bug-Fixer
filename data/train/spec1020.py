import numpy as np 

def function(x):

	c4 = 4
	x9 = x
	paths = []
	try:
		if x9 <= 3:
			x = x9/5
			c4 = 6*c4
			x = 2-x
			paths.append(1)
		else:
			c4 = c4/3
			x9 = x/x9
			x9 = x9/c4
			paths.append(2)
		if x9 >= 3:
			c4 = c4+3
			c4 = x-c4
			x9 = 9-x9
			paths.append(3)
		else:
			x9 = 5/x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))