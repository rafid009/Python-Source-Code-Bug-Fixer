import numpy as np 

def function(x):

	o7 = 9
	w0 = 4
	paths = []
	try:
		if o7 >= 2:
			o7 = o7+x
			paths.append(1)
		else:
			o7 = 7*o7
			x = 7/o7
			w0 = w0*x
			paths.append(2)
		if w0 <= 6:
			w0 = 7+o7
			o7 = o7-o7
			o7 = o7-4
			paths.append(3)
		else:
			w0 = 7+w0
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