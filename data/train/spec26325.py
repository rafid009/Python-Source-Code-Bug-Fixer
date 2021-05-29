import numpy as np 

def function(x):

	c0 = 2
	i1 = x
	paths = []
	try:
		if c0 > 8:
			c0 = c0/2
			paths.append(1)
		else:
			c0 = c0+2
			c0 = c0-c0
			x = x+6
			paths.append(2)
		if c0 >= 8:
			x = x*6
			paths.append(3)
		else:
			c0 = c0+7
			c0 = 1*i1
			i1 = 4-i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))