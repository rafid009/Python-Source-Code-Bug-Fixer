import numpy as np 

def function(x):

	c3 = x
	e7 = 1
	paths = []
	try:
		if c3 >= 2:
			x = x-6
			e7 = c3*6
			paths.append(1)
		else:
			x = e7/5
			paths.append(2)
		if e7 >= 0:
			e7 = 4*e7
			x = c3-9
			e7 = e7*e7
			paths.append(3)
		else:
			x = c3*0
			e7 = 3*e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))