import numpy as np 

def function(x):

	t3 = 7
	w0 = x
	paths = []
	try:
		if x >= 6:
			x = x/4
			paths.append(1)
		else:
			t3 = t3*7
			x = x/3
			w0 = w0/x
			paths.append(2)
		if x > 3:
			w0 = w0+7
			paths.append(3)
		else:
			w0 = w0*t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))