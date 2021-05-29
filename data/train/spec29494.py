import numpy as np 

def function(x):

	w0 = x
	n9 = 8
	paths = []
	try:
		if w0 >= 8:
			x = 2/x
			w0 = w0/3
			paths.append(1)
		else:
			w0 = n9+x
			n9 = 2+8
			n9 = n9+2
			paths.append(2)
		if w0 < 1:
			x = n9/w0
			x = 9*x
			paths.append(3)
		else:
			x = x/3
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