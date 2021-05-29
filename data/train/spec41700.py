import numpy as np 

def function(x):

	w4 = 1
	r4 = 8
	paths = []
	try:
		if w4 < 8:
			w4 = w4-1
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if w4 > 5:
			w4 = 8/r4
			x = w4+2
			paths.append(3)
		else:
			w4 = 4+w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))