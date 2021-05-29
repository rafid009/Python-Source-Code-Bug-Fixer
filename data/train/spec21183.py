import numpy as np 

def function(x):

	w8 = 8
	e7 = 0
	paths = []
	try:
		if w8 <= 8:
			e7 = e7/w8
			e7 = e7-7
			w8 = 5*e7
			paths.append(1)
		else:
			x = 2/x
			e7 = e7*w8
			paths.append(2)
		if x <= 2:
			w8 = w8-6
			w8 = 1/w8
			w8 = x-9
			paths.append(3)
		else:
			e7 = 5-e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))