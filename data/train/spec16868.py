import numpy as np 

def function(x):

	c6 = 3
	x1 = x
	paths = []
	try:
		if x1 > 1:
			c6 = c6/3
			paths.append(1)
		else:
			c6 = 1/x1
			c6 = c6-x
			paths.append(2)
		if c6 > 5:
			c6 = x1*3
			paths.append(3)
		else:
			x1 = x*6
			x1 = 2/8
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x1 = c6**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))