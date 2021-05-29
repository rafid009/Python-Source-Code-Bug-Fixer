import numpy as np 

def function(x):

	o2 = 9
	c3 = 0
	paths = []
	try:
		if c3 < 2:
			c3 = c3+5
			x = x-5
			paths.append(1)
		else:
			c3 = c3/9
			c3 = 4*c3
			paths.append(2)
		if c3 < 2:
			c3 = 8*c3
			paths.append(3)
		else:
			o2 = x-2
			o2 = 2-o2
			c3 = c3-c3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))