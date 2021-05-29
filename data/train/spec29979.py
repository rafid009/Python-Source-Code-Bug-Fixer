import numpy as np 

def function(x):

	q8 = x
	w0 = 1
	paths = []
	try:
		if q8 <= 7:
			q8 = q8*q8
			paths.append(1)
		else:
			q8 = q8*7
			paths.append(2)
		if q8 >= 4:
			x = x/5
			w0 = q8+w0
			x = x*x
			paths.append(3)
		else:
			w0 = w0+6
			q8 = 7-8
			w0 = q8+w0
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		w0 = q8**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))