import numpy as np 

def function(x):

	x5 = x
	w0 = x
	paths = []
	try:
		if w0 < 7:
			x = w0*x
			paths.append(1)
		else:
			x5 = 9-x5
			x = 2/x
			paths.append(2)
		if x < 0:
			x5 = x5*6
			x5 = x5-x
			paths.append(3)
		else:
			x5 = 9+x5
			x5 = x5+6
			x5 = 0/1
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