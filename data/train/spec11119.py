import numpy as np 

def function(x):

	c6 = 5
	c7 = 0
	x = 4
	paths = []
	try:
		if x > 6:
			c7 = c6*4
			paths.append(1)
		else:
			x = 1*c6
			c7 = x/2
			paths.append(2)
		if x < 9:
			c6 = c7-c6
			paths.append(3)
		else:
			c6 = c6-9
			c7 = c7+c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))