import numpy as np 

def function(x):

	w4 = 0
	r7 = 4
	paths = []
	try:
		if r7 > 4:
			w4 = 7+w4
			x = 3*w4
			paths.append(1)
		else:
			x = x-w4
			w4 = w4*4
			w4 = w4/r7
			paths.append(2)
		if r7 < 7:
			r7 = 6/r7
			w4 = 1*x
			paths.append(3)
		else:
			w4 = 9/x
			w4 = r7-r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))