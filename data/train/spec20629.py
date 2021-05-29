import numpy as np 

def function(x):

	e3 = 0
	h0 = 9
	paths = []
	try:
		if x > 9:
			h0 = e3+e3
			paths.append(1)
		else:
			h0 = 5-h0
			paths.append(2)
		if x >= 6:
			e3 = 3*x
			x = x+3
			paths.append(3)
		else:
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))