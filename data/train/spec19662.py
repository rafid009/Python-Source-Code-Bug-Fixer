import numpy as np 

def function(x):

	w0 = 5
	d0 = x
	x = x
	paths = []
	try:
		if x > 5:
			d0 = d0*9
			paths.append(1)
		else:
			x = 5+x
			x = 0/7
			paths.append(2)
		if d0 < 0:
			d0 = d0/w0
			w0 = d0*w0
			x = x+x
			paths.append(3)
		else:
			d0 = 4*d0
			d0 = d0+w0
			x = d0/7
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