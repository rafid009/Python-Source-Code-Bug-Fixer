import numpy as np 

def function(x):

	o4 = x
	w0 = 2
	paths = []
	try:
		if o4 >= 1:
			w0 = x/w0
			w0 = 9*w0
			o4 = 7-o4
			paths.append(1)
		else:
			w0 = w0+x
			x = w0*x
			o4 = o4*9
			paths.append(2)
		if w0 >= 4:
			x = 7/x
			w0 = 7-7
			w0 = 2-x
			paths.append(3)
		else:
			o4 = w0*1
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