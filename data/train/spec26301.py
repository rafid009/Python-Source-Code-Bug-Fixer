import numpy as np 

def function(x):

	w0 = 0
	o9 = x
	paths = []
	try:
		if o9 < 3:
			w0 = 0+o9
			w0 = w0/w0
			paths.append(1)
		else:
			o9 = x+o9
			paths.append(2)
		if w0 < 2:
			w0 = w0/o9
			x = w0/o9
			paths.append(3)
		else:
			x = x/5
			x = x/o9
			x = x+w0
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))