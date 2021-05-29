import numpy as np 

def function(x):

	b2 = x
	w0 = x
	paths = []
	try:
		if b2 <= 2:
			w0 = w0*9
			w0 = 8+w0
			paths.append(1)
		else:
			x = 3-2
			w0 = 3*8
			x = x+6
			paths.append(2)
		if w0 <= 6:
			w0 = 6+w0
			w0 = w0*1
			paths.append(3)
		else:
			x = x-7
			w0 = 9-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))