import numpy as np 

def function(x):

	u6 = x
	c1 = x
	paths = []
	try:
		if c1 < 1:
			c1 = 3+c1
			c1 = c1*c1
			x = 6-x
			paths.append(1)
		else:
			c1 = 0-c1
			c1 = c1-c1
			paths.append(2)
		if x <= 6:
			c1 = c1-c1
			c1 = 2*7
			paths.append(3)
		else:
			u6 = u6-1
			c1 = c1+7
			u6 = 5-u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))