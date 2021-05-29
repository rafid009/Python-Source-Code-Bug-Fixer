import numpy as np 

def function(x):

	w4 = x
	j8 = 9
	paths = []
	try:
		if w4 <= 1:
			w4 = w4+5
			w4 = j8*w4
			w4 = w4-0
			paths.append(1)
		else:
			x = w4+0
			w4 = w4*8
			j8 = 8/j8
			paths.append(2)
		if j8 <= 8:
			x = 4-w4
			w4 = w4+6
			paths.append(3)
		else:
			x = x-5
			j8 = 7/j8
			x = x-w4
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