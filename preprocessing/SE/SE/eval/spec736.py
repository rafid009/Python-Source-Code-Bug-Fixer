import numpy as np 

def function(x):

	w0 = 4
	i8 = x
	paths = []
	try:
		if i8 <= 0:
			i8 = i8-w0
			paths.append(1)
		else:
			x = x-8
			w0 = w0*w0
			i8 = i8*i8
			paths.append(2)
		if w0 <= 4:
			x = 9*7
			x = x+2
			paths.append(3)
		else:
			i8 = i8-x
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		w0 = i8**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))