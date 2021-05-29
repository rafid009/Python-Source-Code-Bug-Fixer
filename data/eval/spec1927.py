import numpy as np 

def function(x):

	j8 = 6
	w0 = 9
	paths = []
	try:
		if j8 >= 4:
			j8 = j8+j8
			x = 7+x
			j8 = j8+w0
			paths.append(1)
		else:
			j8 = j8-9
			paths.append(2)
		if w0 < 5:
			w0 = w0-w0
			paths.append(3)
		else:
			x = 3*x
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))