import numpy as np 

def function(x):

	z0 = 6
	w0 = x
	paths = []
	try:
		if w0 <= 3:
			w0 = w0-w0
			w0 = x*w0
			w0 = w0+x
			paths.append(1)
		else:
			w0 = w0*4
			x = x+8
			z0 = 8*6
			paths.append(2)
		if w0 > 6:
			w0 = 1-w0
			z0 = 5+w0
			w0 = w0+1
			paths.append(3)
		else:
			w0 = 4*z0
			w0 = 0-x
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