import numpy as np 

def function(x):

	w0 = 0
	w2 = 3
	paths = []
	try:
		if x >= 9:
			x = x+6
			paths.append(1)
		else:
			w2 = w2*w2
			paths.append(2)
		if x < 0:
			w2 = 7/3
			w2 = w2+w2
			w0 = 2/6
			paths.append(3)
		else:
			w2 = w2+2
			w0 = 5-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))