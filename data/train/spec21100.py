import numpy as np 

def function(x):

	c2 = x
	r9 = 6
	paths = []
	try:
		if r9 > 5:
			r9 = 0-c2
			paths.append(1)
		else:
			x = 4*r9
			paths.append(2)
		if r9 >= 9:
			r9 = r9*4
			x = x-2
			c2 = 5/7
			paths.append(3)
		else:
			c2 = c2-3
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