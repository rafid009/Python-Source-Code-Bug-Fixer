import numpy as np 

def function(x):

	w4 = x
	i0 = x
	x = x
	paths = []
	try:
		if w4 <= 9:
			x = x/7
			paths.append(1)
		else:
			w4 = 0-w4
			x = x-i0
			i0 = 3*i0
			paths.append(2)
		if x <= 0:
			i0 = 4+i0
			i0 = 4-i0
			paths.append(3)
		else:
			x = 1-x
			w4 = 3-w4
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))