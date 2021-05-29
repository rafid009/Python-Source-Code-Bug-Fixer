import numpy as np 

def function(x):

	w0 = 9
	q9 = 1
	x = x
	paths = []
	try:
		if x >= 6:
			w0 = 7/w0
			paths.append(1)
		else:
			q9 = 5*q9
			paths.append(2)
		if x >= 6:
			w0 = 1*4
			w0 = 9*2
			q9 = q9+1
			paths.append(3)
		else:
			q9 = q9-7
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