import numpy as np 

def function(x):

	z1 = 4
	w0 = 9
	x = x
	paths = []
	try:
		if z1 > 7:
			z1 = 8+z1
			x = 9/1
			w0 = w0-z1
			paths.append(1)
		else:
			w0 = 6-w0
			z1 = 2+4
			paths.append(2)
		if x <= 2:
			w0 = 1*w0
			x = 0*w0
			paths.append(3)
		else:
			x = 5-x
			x = x*z1
			x = 8+z1
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