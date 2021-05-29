import numpy as np 

def function(x):

	v9 = 7
	e7 = x
	x = 7
	paths = []
	try:
		if e7 <= 1:
			v9 = v9*9
			v9 = v9/3
			paths.append(1)
		else:
			x = 4*x
			e7 = 1*e7
			paths.append(2)
		if e7 <= 1:
			x = 3+e7
			e7 = e7/3
			paths.append(3)
		else:
			x = x*x
			e7 = 0-e7
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