import numpy as np 

def function(x):

	v3 = x
	w0 = x
	paths = []
	try:
		if w0 < 7:
			v3 = v3*7
			w0 = w0*2
			paths.append(1)
		else:
			x = x-x
			w0 = w0/8
			x = 9-w0
			paths.append(2)
		if v3 <= 9:
			w0 = w0*2
			paths.append(3)
		else:
			x = v3-x
			x = 9-w0
			v3 = 3*v3
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