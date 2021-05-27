import numpy as np 

def function(x):

	i0 = 6
	c6 = x
	paths = []
	try:
		if c6 > 3:
			c6 = 8+c6
			paths.append(1)
		else:
			x = x/c6
			c6 = 2/8
			paths.append(2)
		if c6 > 1:
			c6 = x*2
			i0 = i0-x
			c6 = c6/6
			paths.append(3)
		else:
			i0 = 0-4
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))