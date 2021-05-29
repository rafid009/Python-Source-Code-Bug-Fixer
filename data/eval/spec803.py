import numpy as np 

def function(x):

	c4 = 0
	j0 = x
	paths = []
	try:
		if j0 >= 1:
			x = x-3
			paths.append(1)
		else:
			x = x-j0
			c4 = c4/8
			paths.append(2)
		if c4 > 0:
			x = x/9
			x = x+0
			paths.append(3)
		else:
			j0 = 7*j0
			c4 = c4+j0
			j0 = j0+j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))