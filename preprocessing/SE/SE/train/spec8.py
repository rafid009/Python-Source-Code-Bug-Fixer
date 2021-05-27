import numpy as np 

def function(x):

	w4 = 2
	e0 = x
	paths = []
	try:
		if x <= 9:
			x = 7*x
			w4 = e0-0
			w4 = 8/e0
			paths.append(1)
		else:
			e0 = e0*6
			e0 = 7-3
			paths.append(2)
		if x < 0:
			w4 = w4*x
			x = 4/x
			paths.append(3)
		else:
			x = w4+x
			e0 = e0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))