import numpy as np 

def function(x):

	a9 = x
	e3 = 0
	paths = []
	try:
		if x < 5:
			a9 = a9-e3
			paths.append(1)
		else:
			x = 5-3
			a9 = a9*8
			paths.append(2)
		if x >= 6:
			e3 = 0*3
			x = x-a9
			paths.append(3)
		else:
			a9 = a9+2
			x = x-9
			e3 = 9+e3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))