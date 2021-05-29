import numpy as np 

def function(x):

	w0 = x
	k0 = x
	paths = []
	try:
		if k0 > 4:
			w0 = 7-w0
			paths.append(1)
		else:
			x = x/2
			k0 = 3/1
			x = x/k0
			paths.append(2)
		if w0 > 1:
			w0 = 9-6
			k0 = x-7
			paths.append(3)
		else:
			k0 = x-k0
			x = k0-4
			k0 = k0+k0
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