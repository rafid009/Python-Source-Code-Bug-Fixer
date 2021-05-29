import numpy as np 

def function(x):

	w0 = 5
	d8 = 3
	paths = []
	try:
		if x <= 1:
			w0 = 6*w0
			x = w0/w0
			paths.append(1)
		else:
			d8 = x-d8
			paths.append(2)
		if x < 4:
			d8 = d8*3
			w0 = 8*w0
			paths.append(3)
		else:
			w0 = w0-8
			x = x/9
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