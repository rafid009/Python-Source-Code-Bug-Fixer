import numpy as np 

def function(x):

	w0 = 3
	q3 = x
	paths = []
	try:
		if q3 >= 2:
			q3 = q3/6
			x = x-0
			w0 = 7-w0
			paths.append(1)
		else:
			x = x*q3
			w0 = x+w0
			paths.append(2)
		if q3 > 9:
			w0 = w0+2
			paths.append(3)
		else:
			w0 = q3*w0
			q3 = w0-5
			x = x+9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		w0 = q3**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))