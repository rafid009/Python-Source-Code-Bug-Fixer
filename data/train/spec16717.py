import numpy as np 

def function(x):

	e2 = x
	c5 = 5
	paths = []
	try:
		if c5 < 3:
			x = x+9
			paths.append(1)
		else:
			c5 = x+0
			paths.append(2)
		if e2 >= 5:
			x = x*3
			x = 6-3
			paths.append(3)
		else:
			c5 = 8-0
			e2 = 5-e2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))