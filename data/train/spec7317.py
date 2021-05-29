import numpy as np 

def function(x):

	e3 = 3
	w0 = 9
	paths = []
	try:
		if e3 >= 7:
			e3 = e3/7
			paths.append(1)
		else:
			x = x*7
			x = 0-e3
			paths.append(2)
		if x < 1:
			e3 = 8*e3
			w0 = w0+5
			e3 = e3+w0
			paths.append(3)
		else:
			w0 = 7-w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))