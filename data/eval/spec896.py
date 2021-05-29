import numpy as np 

def function(x):

	c8 = 0
	n2 = x
	x = x
	paths = []
	try:
		if n2 >= 6:
			c8 = x-n2
			paths.append(1)
		else:
			x = 1/x
			c8 = c8*c8
			paths.append(2)
		if x > 2:
			x = c8+0
			n2 = n2+2
			c8 = 1-c8
			paths.append(3)
		else:
			c8 = c8*8
			c8 = c8*c8
			x = x/3
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