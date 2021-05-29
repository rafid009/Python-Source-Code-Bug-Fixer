import numpy as np 

def function(x):

	w0 = x
	b1 = 9
	paths = []
	try:
		if b1 <= 4:
			w0 = w0+w0
			paths.append(1)
		else:
			x = 2-5
			b1 = 6/b1
			paths.append(2)
		if x >= 1:
			w0 = w0*0
			w0 = w0+6
			paths.append(3)
		else:
			b1 = b1-4
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