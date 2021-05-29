import numpy as np 

def function(x):

	e4 = 0
	a4 = 9
	paths = []
	try:
		if a4 < 1:
			a4 = a4-6
			e4 = e4/e4
			x = e4*8
			paths.append(1)
		else:
			x = 3*x
			e4 = 8+e4
			e4 = 7-3
			paths.append(2)
		if a4 < 8:
			e4 = 3+e4
			x = x-x
			paths.append(3)
		else:
			e4 = a4*7
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))