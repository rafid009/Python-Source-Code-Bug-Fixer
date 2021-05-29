import numpy as np 

def function(x):

	w0 = x
	f3 = 3
	paths = []
	try:
		if w0 <= 2:
			f3 = f3*x
			x = 3-x
			paths.append(1)
		else:
			f3 = f3-6
			paths.append(2)
		if w0 <= 6:
			f3 = f3/x
			paths.append(3)
		else:
			f3 = f3-f3
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