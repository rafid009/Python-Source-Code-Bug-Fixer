import numpy as np 

def function(x):

	w0 = x
	b2 = 4
	paths = []
	try:
		if w0 <= 9:
			w0 = 3+9
			w0 = w0*6
			paths.append(1)
		else:
			x = b2-b2
			paths.append(2)
		if b2 > 3:
			b2 = b2+3
			w0 = 7-w0
			w0 = 8-w0
			paths.append(3)
		else:
			b2 = b2*2
			x = 6-9
			x = 9/x
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