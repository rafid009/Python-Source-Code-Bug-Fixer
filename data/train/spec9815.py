import numpy as np 

def function(x):

	e1 = x
	c3 = x
	paths = []
	try:
		if x <= 8:
			c3 = 0+8
			e1 = e1-2
			paths.append(1)
		else:
			x = 9+x
			x = 4-x
			x = x/9
			paths.append(2)
		if c3 <= 2:
			e1 = 5+e1
			c3 = 2-c3
			paths.append(3)
		else:
			c3 = c3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))