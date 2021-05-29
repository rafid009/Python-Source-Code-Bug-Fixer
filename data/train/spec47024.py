import numpy as np 

def function(x):

	c7 = 9
	u7 = 6
	paths = []
	try:
		if c7 <= 9:
			x = 5/x
			u7 = 3-c7
			paths.append(1)
		else:
			c7 = c7/8
			u7 = 8+5
			paths.append(2)
		if x < 0:
			x = 3-3
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))