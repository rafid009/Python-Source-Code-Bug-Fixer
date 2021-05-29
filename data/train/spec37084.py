import numpy as np 

def function(x):

	v3 = x
	c4 = 7
	paths = []
	try:
		if c4 > 5:
			x = 0-2
			paths.append(1)
		else:
			c4 = c4-1
			c4 = 4-c4
			paths.append(2)
		if c4 <= 9:
			x = v3*c4
			c4 = c4*7
			v3 = v3+0
			paths.append(3)
		else:
			x = 5+8
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