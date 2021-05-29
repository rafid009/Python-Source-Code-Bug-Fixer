import numpy as np 

def function(x):

	h5 = x
	v8 = 2
	paths = []
	try:
		if x >= 3:
			h5 = h5-4
			v8 = v8-1
			paths.append(1)
		else:
			h5 = h5-0
			paths.append(2)
		if h5 <= 9:
			h5 = 7+v8
			paths.append(3)
		else:
			x = h5+x
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