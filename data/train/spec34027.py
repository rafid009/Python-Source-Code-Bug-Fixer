import numpy as np 

def function(x):

	e2 = x
	w0 = 9
	paths = []
	try:
		if e2 < 6:
			e2 = e2-9
			x = 8-8
			paths.append(1)
		else:
			e2 = e2*7
			x = w0*3
			x = x/x
			paths.append(2)
		if x > 6:
			e2 = 2-e2
			e2 = 2-e2
			w0 = x-7
			paths.append(3)
		else:
			w0 = w0-8
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))