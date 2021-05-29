import numpy as np 

def function(x):

	w0 = x
	y9 = 7
	paths = []
	try:
		if w0 >= 7:
			y9 = 2-y9
			x = w0*x
			x = 3/x
			paths.append(1)
		else:
			x = 3+x
			y9 = 2*x
			paths.append(2)
		if w0 > 0:
			x = x+x
			x = x-w0
			paths.append(3)
		else:
			y9 = y9*0
			x = 6-x
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