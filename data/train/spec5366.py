import numpy as np 

def function(x):

	j7 = 4
	w0 = 2
	paths = []
	try:
		if j7 < 6:
			w0 = w0+x
			w0 = w0*j7
			paths.append(1)
		else:
			x = x-9
			x = 0-7
			x = j7-x
			paths.append(2)
		if w0 > 0:
			j7 = j7+8
			paths.append(3)
		else:
			x = x+x
			w0 = 7/w0
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