import numpy as np 

def function(x):

	e5 = x
	c5 = x
	paths = []
	try:
		if x >= 5:
			c5 = c5+9
			c5 = 5/c5
			e5 = 7/x
			paths.append(1)
		else:
			c5 = 3/c5
			paths.append(2)
		if e5 < 7:
			c5 = 0/c5
			paths.append(3)
		else:
			c5 = x*c5
			c5 = c5-x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))