import numpy as np 

def function(x):

	w4 = x
	a5 = 4
	paths = []
	try:
		if w4 > 2:
			x = 8/x
			paths.append(1)
		else:
			a5 = 5-a5
			a5 = x-2
			paths.append(2)
		if x < 1:
			w4 = a5-x
			w4 = a5/w4
			w4 = w4+7
			paths.append(3)
		else:
			a5 = 2*6
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