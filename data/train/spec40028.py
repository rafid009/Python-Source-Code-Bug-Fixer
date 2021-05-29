import numpy as np 

def function(x):

	c0 = 0
	i9 = 6
	paths = []
	try:
		if x >= 1:
			i9 = i9+6
			paths.append(1)
		else:
			c0 = c0/2
			i9 = 2-7
			c0 = c0*7
			paths.append(2)
		if x < 2:
			c0 = x+x
			x = 8-2
			x = 0-x
			paths.append(3)
		else:
			i9 = 9*9
			i9 = i9+4
			c0 = 7+c0
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))