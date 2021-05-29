import numpy as np 

def function(x):

	v1 = 2
	e7 = 8
	paths = []
	try:
		if v1 <= 6:
			e7 = 9+7
			paths.append(1)
		else:
			x = 2/x
			e7 = 0+e7
			e7 = e7*e7
			paths.append(2)
		if x > 6:
			x = 7/e7
			x = x+4
			e7 = 6*9
			paths.append(3)
		else:
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))