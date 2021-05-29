import numpy as np 

def function(x):

	w0 = 4
	o1 = x
	paths = []
	try:
		if w0 <= 4:
			x = 3+x
			o1 = 4/o1
			paths.append(1)
		else:
			w0 = o1*w0
			x = 0/x
			x = o1+x
			paths.append(2)
		if o1 > 8:
			o1 = o1*8
			x = x/o1
			o1 = o1+o1
			paths.append(3)
		else:
			w0 = 0*2
			w0 = 4-w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))