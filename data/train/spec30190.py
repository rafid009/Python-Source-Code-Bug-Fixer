import numpy as np 

def function(x):

	w0 = 5
	h9 = 9
	paths = []
	try:
		if w0 >= 4:
			w0 = 5+0
			paths.append(1)
		else:
			h9 = h9-1
			w0 = 6-w0
			paths.append(2)
		if x <= 7:
			h9 = 5-h9
			h9 = 3*h9
			paths.append(3)
		else:
			w0 = 2/w0
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		w0 = h9**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))