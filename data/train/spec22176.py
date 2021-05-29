import numpy as np 

def function(x):

	c3 = 3
	e9 = x
	x = x
	paths = []
	try:
		if e9 > 9:
			e9 = 6-e9
			c3 = 7+x
			c3 = x/c3
			paths.append(1)
		else:
			e9 = 3+6
			e9 = e9+c3
			c3 = c3+7
			paths.append(2)
		if x >= 8:
			c3 = 6-c3
			paths.append(3)
		else:
			c3 = 4+c3
			c3 = c3-c3
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