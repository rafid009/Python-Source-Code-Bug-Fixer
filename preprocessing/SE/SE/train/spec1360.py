import numpy as np 

def function(x):

	c9 = x
	e5 = x
	x = x
	paths = []
	try:
		if e5 >= 6:
			c9 = 0/e5
			paths.append(1)
		else:
			x = c9/x
			paths.append(2)
		if x > 8:
			x = 2+x
			paths.append(3)
		else:
			c9 = c9-e5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))