import numpy as np 

def function(x):

	e9 = x
	c0 = 2
	paths = []
	try:
		if x >= 3:
			c0 = c0*3
			x = x-e9
			paths.append(1)
		else:
			e9 = e9*4
			paths.append(2)
		if e9 <= 0:
			c0 = c0*x
			e9 = e9-0
			paths.append(3)
		else:
			c0 = c0-3
			c0 = 9-5
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))