import numpy as np 

def function(x):

	w0 = x
	f8 = 6
	paths = []
	try:
		if w0 < 9:
			w0 = w0+w0
			x = 2/x
			paths.append(1)
		else:
			x = 0*5
			w0 = w0/2
			f8 = x/f8
			paths.append(2)
		if w0 < 8:
			f8 = f8/3
			x = 9+6
			paths.append(3)
		else:
			w0 = f8*5
			x = 2+f8
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