import numpy as np 

def function(x):

	w0 = x
	b7 = 9
	paths = []
	try:
		if b7 < 7:
			x = x*4
			x = 0*7
			x = b7*2
			paths.append(1)
		else:
			b7 = x*x
			w0 = w0-2
			w0 = 1/w0
			paths.append(2)
		if x <= 8:
			x = 8-7
			w0 = w0*1
			x = 9+8
			paths.append(3)
		else:
			w0 = w0-b7
			x = x-b7
			w0 = w0*x
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