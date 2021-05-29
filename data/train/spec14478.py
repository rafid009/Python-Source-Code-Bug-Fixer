import numpy as np 

def function(x):

	e6 = x
	c7 = x
	paths = []
	try:
		if x <= 6:
			e6 = x/c7
			paths.append(1)
		else:
			e6 = e6*e6
			c7 = e6-c7
			paths.append(2)
		if x < 5:
			e6 = 1+e6
			e6 = 0+3
			x = 5/x
			paths.append(3)
		else:
			e6 = e6+0
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))