import numpy as np 

def function(x):

	j6 = x
	w0 = 3
	paths = []
	try:
		if j6 >= 5:
			w0 = 9-w0
			j6 = 0*j6
			x = 9+j6
			paths.append(1)
		else:
			j6 = 9*w0
			w0 = 3/x
			x = j6+x
			paths.append(2)
		if j6 > 5:
			j6 = w0+j6
			paths.append(3)
		else:
			x = 3-0
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