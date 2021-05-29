import numpy as np 

def function(x):

	w0 = x
	n8 = 1
	paths = []
	try:
		if x < 1:
			n8 = 5+n8
			w0 = 0+1
			x = x-9
			paths.append(1)
		else:
			n8 = n8-w0
			x = x*x
			paths.append(2)
		if w0 > 8:
			w0 = w0+5
			w0 = n8*x
			x = w0+9
			paths.append(3)
		else:
			w0 = w0+2
			w0 = x/9
			w0 = w0*w0
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