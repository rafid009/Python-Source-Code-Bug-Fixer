import numpy as np 

def function(x):

	a1 = 1
	w0 = 5
	paths = []
	try:
		if x >= 7:
			a1 = 9+a1
			a1 = a1/x
			a1 = 6-w0
			paths.append(1)
		else:
			w0 = a1+x
			w0 = w0+7
			a1 = a1/5
			paths.append(2)
		if a1 > 6:
			w0 = a1*w0
			paths.append(3)
		else:
			a1 = a1+0
			a1 = 3*1
			w0 = w0/5
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