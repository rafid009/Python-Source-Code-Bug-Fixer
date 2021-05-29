import numpy as np 

def function(x):

	w0 = 8
	a7 = x
	paths = []
	try:
		if x < 4:
			a7 = 7-3
			a7 = a7+5
			paths.append(1)
		else:
			w0 = w0+w0
			paths.append(2)
		if x > 9:
			a7 = x*w0
			x = 6/x
			w0 = 3-w0
			paths.append(3)
		else:
			w0 = w0+5
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))