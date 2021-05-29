import numpy as np 

def function(x):

	k9 = 4
	w0 = 9
	paths = []
	try:
		if w0 < 9:
			x = 1/9
			w0 = k9-1
			w0 = 7+2
			paths.append(1)
		else:
			k9 = k9+w0
			w0 = 6/w0
			k9 = k9/x
			paths.append(2)
		if k9 < 0:
			x = x+6
			w0 = w0+8
			paths.append(3)
		else:
			x = 7+x
			w0 = k9+0
			k9 = 4-k9
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