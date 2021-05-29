import numpy as np 

def function(x):

	w0 = x
	k7 = 9
	paths = []
	try:
		if x <= 2:
			w0 = w0*1
			k7 = 7+k7
			paths.append(1)
		else:
			w0 = w0/w0
			x = 3+x
			x = 9/x
			paths.append(2)
		if x <= 6:
			x = 2/8
			k7 = 4*w0
			x = x-4
			paths.append(3)
		else:
			w0 = 7-w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))