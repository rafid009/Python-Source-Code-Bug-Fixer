import numpy as np 

def function(x):

	c7 = x
	n8 = 7
	paths = []
	try:
		if n8 >= 3:
			x = c7+n8
			c7 = c7-7
			paths.append(1)
		else:
			c7 = n8+8
			c7 = c7+7
			paths.append(2)
		if n8 >= 9:
			c7 = n8-c7
			paths.append(3)
		else:
			c7 = c7-7
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