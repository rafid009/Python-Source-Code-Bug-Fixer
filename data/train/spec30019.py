import numpy as np 

def function(x):

	e1 = x
	c6 = 3
	paths = []
	try:
		if x < 5:
			x = x+4
			paths.append(1)
		else:
			e1 = 0*e1
			paths.append(2)
		if e1 <= 4:
			c6 = 1*x
			paths.append(3)
		else:
			e1 = 8/e1
			e1 = e1-4
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