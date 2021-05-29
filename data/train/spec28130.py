import numpy as np 

def function(x):

	e5 = 8
	c6 = x
	paths = []
	try:
		if x > 0:
			x = 5-x
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if c6 <= 9:
			c6 = c6+3
			c6 = c6+4
			paths.append(3)
		else:
			x = e5/x
			x = x-x
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