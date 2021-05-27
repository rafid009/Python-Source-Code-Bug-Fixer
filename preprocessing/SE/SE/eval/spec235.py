import numpy as np 

def function(x):

	c9 = 5
	w4 = x
	paths = []
	try:
		if c9 > 0:
			w4 = w4-6
			paths.append(1)
		else:
			c9 = c9-0
			w4 = w4*5
			w4 = x-3
			paths.append(2)
		if x > 5:
			c9 = 8-c9
			paths.append(3)
		else:
			w4 = 7*w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))