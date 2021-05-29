import numpy as np 

def function(x):

	c6 = x
	x6 = 2
	x = x
	paths = []
	try:
		if x >= 7:
			x6 = x6+9
			paths.append(1)
		else:
			x = 9+x
			x6 = x6-x
			paths.append(2)
		if x > 3:
			x6 = c6+x6
			c6 = 8+c6
			paths.append(3)
		else:
			x6 = 1/c6
			c6 = x/4
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