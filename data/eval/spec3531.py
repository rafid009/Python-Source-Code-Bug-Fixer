import numpy as np 

def function(x):

	n4 = 2
	c7 = x
	paths = []
	try:
		if x <= 3:
			c7 = n4/6
			paths.append(1)
		else:
			c7 = 8-c7
			c7 = c7-x
			paths.append(2)
		if c7 <= 0:
			c7 = 2*c7
			paths.append(3)
		else:
			x = c7*x
			n4 = 8+n4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))