import numpy as np 

def function(x):

	c4 = x
	u5 = 5
	x = 2
	paths = []
	try:
		if c4 >= 3:
			x = x/7
			paths.append(1)
		else:
			x = 6-u5
			paths.append(2)
		if x >= 0:
			u5 = u5*u5
			paths.append(3)
		else:
			x = 8*x
			x = 0+4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))