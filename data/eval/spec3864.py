import numpy as np 

def function(x):

	w0 = x
	a9 = x
	paths = []
	try:
		if x > 3:
			w0 = x*w0
			w0 = w0/9
			paths.append(1)
		else:
			x = w0-x
			paths.append(2)
		if w0 <= 3:
			x = w0-w0
			paths.append(3)
		else:
			x = x/w0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		a9 = w0**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))