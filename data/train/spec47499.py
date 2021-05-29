import numpy as np 

def function(x):

	d4 = 5
	w0 = 6
	paths = []
	try:
		if w0 > 6:
			d4 = 2/d4
			w0 = w0-5
			x = x/4
			paths.append(1)
		else:
			d4 = 0-3
			x = 2+7
			paths.append(2)
		if x > 0:
			x = 7+x
			d4 = d4-3
			paths.append(3)
		else:
			w0 = 3+w0
			x = 6/w0
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))