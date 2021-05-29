import numpy as np 

def function(x):

	d2 = 1
	w4 = 7
	paths = []
	try:
		if x >= 2:
			x = 5*x
			w4 = w4-0
			paths.append(1)
		else:
			d2 = 2/8
			paths.append(2)
		if d2 >= 0:
			d2 = d2/d2
			paths.append(3)
		else:
			x = 7-w4
			w4 = 1*d2
			x = w4*x
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