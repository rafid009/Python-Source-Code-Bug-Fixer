import numpy as np 

def function(x):

	w7 = x
	x5 = x
	paths = []
	try:
		if x5 <= 2:
			x5 = x/x5
			paths.append(1)
		else:
			x = x-w7
			paths.append(2)
		if x >= 9:
			x = 3/6
			x5 = 6*x5
			x5 = 8-w7
			paths.append(3)
		else:
			x5 = 1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))