import numpy as np 

def function(x):

	y3 = 8
	c2 = 0
	paths = []
	try:
		if c2 > 2:
			x = x-c2
			c2 = c2-1
			x = 4-c2
			paths.append(1)
		else:
			c2 = y3-c2
			paths.append(2)
		if c2 >= 6:
			c2 = c2+9
			paths.append(3)
		else:
			x = x+8
			c2 = c2+5
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