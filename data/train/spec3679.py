import numpy as np 

def function(x):

	c0 = 7
	u7 = x
	paths = []
	try:
		if x < 9:
			u7 = 4/u7
			paths.append(1)
		else:
			x = 3/8
			paths.append(2)
		if x < 2:
			x = 3+8
			paths.append(3)
		else:
			u7 = u7+0
			c0 = 6-x
			u7 = 0-u7
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))