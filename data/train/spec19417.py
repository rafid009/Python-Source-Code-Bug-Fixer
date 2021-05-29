import numpy as np 

def function(x):

	e2 = 1
	c6 = x
	paths = []
	try:
		if x >= 1:
			c6 = x-e2
			c6 = c6*2
			e2 = 7/6
			paths.append(1)
		else:
			x = 8*7
			e2 = c6*8
			e2 = 0-4
			paths.append(2)
		if x > 6:
			e2 = e2/8
			x = 0-0
			paths.append(3)
		else:
			c6 = 9-0
			e2 = x-4
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))