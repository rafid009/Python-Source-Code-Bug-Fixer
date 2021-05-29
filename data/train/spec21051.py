import numpy as np 

def function(x):

	e9 = x
	x0 = x
	paths = []
	try:
		if e9 >= 9:
			x0 = 2/4
			e9 = e9+x
			x0 = e9*x0
			paths.append(1)
		else:
			x = x-4
			x0 = 1/x0
			paths.append(2)
		if x0 < 4:
			x0 = 6-7
			e9 = e9+6
			e9 = 8-e9
			paths.append(3)
		else:
			x = x*5
			x = x+0
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