import numpy as np 

def function(x):

	w0 = 7
	d5 = x
	paths = []
	try:
		if w0 < 1:
			w0 = d5/x
			w0 = x+d5
			paths.append(1)
		else:
			d5 = d5-x
			w0 = 5*w0
			paths.append(2)
		if w0 > 2:
			w0 = 5-w0
			d5 = 3+d5
			x = 2*x
			paths.append(3)
		else:
			w0 = 6-x
			x = w0+d5
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w0 = w0**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))