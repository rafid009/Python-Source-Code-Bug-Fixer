import numpy as np 

def function(x):

	e3 = 7
	x6 = x
	paths = []
	try:
		if x > 5:
			x = x/x
			x = 1/x
			paths.append(1)
		else:
			x = 5/x
			x = x6-x
			paths.append(2)
		if x < 5:
			e3 = e3*x
			paths.append(3)
		else:
			x = 3-x
			x6 = 0-3
			e3 = e3-3
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