import numpy as np 

def function(x):

	y7 = 0
	w0 = 4
	paths = []
	try:
		if w0 <= 2:
			y7 = 8*y7
			x = x-y7
			w0 = y7+7
			paths.append(1)
		else:
			w0 = w0+8
			y7 = 1*9
			paths.append(2)
		if x >= 6:
			w0 = w0*x
			x = 4/x
			paths.append(3)
		else:
			y7 = y7/6
			w0 = 1-y7
			x = 2-x
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