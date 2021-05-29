import numpy as np 

def function(x):

	c8 = x
	r8 = x
	paths = []
	try:
		if x < 3:
			x = x+5
			paths.append(1)
		else:
			c8 = c8*c8
			r8 = x+r8
			paths.append(2)
		if c8 >= 9:
			c8 = 0-c8
			paths.append(3)
		else:
			c8 = 8/r8
			r8 = r8+r8
			r8 = 7-1
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