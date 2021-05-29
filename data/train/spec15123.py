import numpy as np 

def function(x):

	c2 = x
	e8 = 6
	paths = []
	try:
		if e8 > 0:
			c2 = 2/1
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if e8 < 9:
			c2 = c2-3
			c2 = x/x
			c2 = e8/c2
			paths.append(3)
		else:
			x = 0+x
			x = 0-0
			e8 = e8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))