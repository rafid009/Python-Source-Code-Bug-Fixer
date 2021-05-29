import numpy as np 

def function(x):

	w0 = x
	q3 = x
	paths = []
	try:
		if x > 1:
			x = x/6
			q3 = q3*9
			x = x*w0
			paths.append(1)
		else:
			q3 = w0-w0
			paths.append(2)
		if q3 < 2:
			w0 = 3-0
			x = q3-2
			paths.append(3)
		else:
			q3 = 9*q3
			x = q3+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))