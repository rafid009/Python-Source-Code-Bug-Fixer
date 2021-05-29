import numpy as np 

def function(x):

	w0 = x
	paths = []
	try:
		if w0 <= 8:
			w0 = 5-w0
			paths.append(1)
		else:
			w0 = w0*x
			w0 = 3-w0
			x = x*1
			paths.append(2)
		if w0 <= 5:
			w0 = w0/3
			w0 = 7+w0
			x = w0/2
			paths.append(3)
		else:
			w0 = w0/2
			w0 = 8*w0
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