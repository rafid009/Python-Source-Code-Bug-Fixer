import numpy as np 

def function(x):

	w0 = x
	v2 = 2
	paths = []
	try:
		if w0 <= 5:
			v2 = 1-v2
			paths.append(1)
		else:
			x = x+4
			x = x+x
			w0 = w0-4
			paths.append(2)
		if x > 6:
			v2 = 3+4
			v2 = v2-v2
			v2 = 0-2
			paths.append(3)
		else:
			w0 = w0+1
			x = x+x
			v2 = 1-v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))