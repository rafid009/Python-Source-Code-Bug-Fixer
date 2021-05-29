import numpy as np 

def function(x):

	x3 = 4
	e2 = 2
	paths = []
	try:
		if x > 0:
			e2 = e2*x3
			x = x*3
			paths.append(1)
		else:
			x3 = x3-2
			x3 = x3-e2
			e2 = e2-4
			paths.append(2)
		if x >= 8:
			x3 = 2/x3
			paths.append(3)
		else:
			x = 7-9
			e2 = e2/7
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