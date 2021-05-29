import numpy as np 

def function(x):

	t0 = x
	e5 = 7
	paths = []
	try:
		if x >= 1:
			x = x/x
			t0 = 7/t0
			paths.append(1)
		else:
			e5 = 7/e5
			paths.append(2)
		if x >= 6:
			t0 = 9+2
			e5 = t0+0
			x = e5+0
			paths.append(3)
		else:
			x = x-0
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