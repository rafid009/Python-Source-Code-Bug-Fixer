import numpy as np 

def function(x):

	n1 = 7
	w0 = 2
	paths = []
	try:
		if n1 < 5:
			n1 = 5+n1
			x = 2*x
			w0 = 9+8
			paths.append(1)
		else:
			n1 = n1+6
			n1 = n1-7
			x = 4/9
			paths.append(2)
		if w0 <= 9:
			w0 = w0-5
			paths.append(3)
		else:
			w0 = w0/x
			n1 = n1-6
			x = 3*6
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