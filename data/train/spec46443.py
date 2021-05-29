import numpy as np 

def function(x):

	w0 = x
	d7 = x
	paths = []
	try:
		if w0 <= 6:
			w0 = w0/2
			paths.append(1)
		else:
			d7 = d7-w0
			x = 2/5
			paths.append(2)
		if x <= 5:
			w0 = w0+w0
			paths.append(3)
		else:
			w0 = 4-1
			x = d7*9
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		d7 = w0**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))