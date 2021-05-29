import numpy as np 

def function(x):

	x0 = x
	w0 = 7
	x = 5
	paths = []
	try:
		if x0 >= 9:
			x0 = 1*8
			x = x/8
			x0 = x0*0
			paths.append(1)
		else:
			x0 = x0*x
			w0 = w0+6
			x0 = x0-8
			paths.append(2)
		if x0 <= 2:
			x = x0+w0
			x0 = 5*x0
			paths.append(3)
		else:
			w0 = 6-w0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))