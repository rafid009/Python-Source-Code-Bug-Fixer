import numpy as np 

def function(x):

	n9 = x
	w0 = 1
	paths = []
	try:
		if x > 0:
			x = 4*x
			n9 = n9*8
			paths.append(1)
		else:
			x = 1*8
			n9 = n9/w0
			paths.append(2)
		if w0 < 2:
			x = 5/x
			x = w0+4
			w0 = w0-x
			paths.append(3)
		else:
			w0 = 9/w0
			x = x/5
			w0 = w0+n9
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