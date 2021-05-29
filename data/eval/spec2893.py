import numpy as np 

def function(x):

	f4 = x
	c3 = x
	paths = []
	try:
		if x >= 8:
			x = 9-c3
			x = 4*x
			paths.append(1)
		else:
			x = x-3
			f4 = x/1
			paths.append(2)
		if c3 < 0:
			c3 = 0/c3
			paths.append(3)
		else:
			c3 = c3*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))