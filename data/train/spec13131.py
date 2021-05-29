import numpy as np 

def function(x):

	y5 = x
	w0 = 3
	paths = []
	try:
		if x <= 4:
			x = 4+x
			paths.append(1)
		else:
			y5 = y5-7
			y5 = w0-7
			paths.append(2)
		if w0 <= 2:
			y5 = y5*7
			paths.append(3)
		else:
			y5 = 9+y5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))