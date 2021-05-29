import numpy as np 

def function(x):

	n9 = 7
	c4 = x
	paths = []
	try:
		if c4 >= 1:
			n9 = 2*5
			c4 = n9-c4
			c4 = 8+6
			paths.append(1)
		else:
			n9 = 7+n9
			x = x-8
			paths.append(2)
		if n9 < 4:
			n9 = c4*n9
			paths.append(3)
		else:
			n9 = x-c4
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))