import numpy as np 

def function(x):

	w0 = x
	x5 = x
	paths = []
	try:
		if x5 <= 3:
			x = 5-w0
			w0 = w0-5
			paths.append(1)
		else:
			w0 = 7/4
			w0 = w0-x5
			x = x*x
			paths.append(2)
		if x5 > 6:
			x = 9*x5
			x5 = 7+x5
			paths.append(3)
		else:
			x5 = x/x5
			x = 2/x
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))