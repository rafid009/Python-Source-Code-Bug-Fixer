import numpy as np 

def function(x):

	w0 = x
	y7 = 5
	x = x
	paths = []
	try:
		if w0 < 7:
			x = x-8
			paths.append(1)
		else:
			w0 = 9*2
			w0 = w0-0
			x = 6*x
			paths.append(2)
		if x > 1:
			w0 = y7/y7
			x = 8*x
			paths.append(3)
		else:
			x = 4+0
			y7 = w0+y7
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		y7 = w0**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))