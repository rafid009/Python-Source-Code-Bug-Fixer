import numpy as np 

def function(x):

	w0 = x
	j7 = 7
	paths = []
	try:
		if j7 >= 1:
			j7 = j7+w0
			j7 = j7-6
			paths.append(1)
		else:
			w0 = 4+j7
			x = x+7
			paths.append(2)
		if w0 >= 9:
			j7 = w0-w0
			paths.append(3)
		else:
			w0 = w0-w0
			w0 = x-w0
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