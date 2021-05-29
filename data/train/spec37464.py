import numpy as np 

def function(x):

	w0 = x
	p8 = x
	paths = []
	try:
		if w0 < 8:
			w0 = 5+p8
			p8 = p8+4
			p8 = 4*1
			paths.append(1)
		else:
			p8 = 3-1
			paths.append(2)
		if x < 3:
			p8 = p8/6
			paths.append(3)
		else:
			x = 2*x
			w0 = p8+x
			w0 = 0-p8
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