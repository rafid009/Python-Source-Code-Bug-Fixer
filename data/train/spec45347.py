import numpy as np 

def function(x):

	u0 = x
	w4 = x
	paths = []
	try:
		if x <= 8:
			u0 = u0+9
			paths.append(1)
		else:
			w4 = 0-3
			x = x-3
			paths.append(2)
		if u0 < 2:
			u0 = u0+2
			x = 6*x
			u0 = u0-2
			paths.append(3)
		else:
			x = 8/x
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