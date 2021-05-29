import numpy as np 

def function(x):

	e4 = x
	e8 = 5
	paths = []
	try:
		if e4 < 6:
			e8 = e4/e8
			e4 = 8*e4
			x = x/4
			paths.append(1)
		else:
			x = 7-9
			paths.append(2)
		if e8 > 6:
			e8 = 9+9
			x = x*e8
			paths.append(3)
		else:
			e4 = 5+e4
			e8 = x-e8
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