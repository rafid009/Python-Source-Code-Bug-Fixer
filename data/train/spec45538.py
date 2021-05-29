import numpy as np 

def function(x):

	k4 = x
	w4 = 7
	paths = []
	try:
		if w4 > 3:
			k4 = 6/k4
			w4 = w4/4
			w4 = w4*8
			paths.append(1)
		else:
			k4 = x-7
			x = 8+8
			x = x*w4
			paths.append(2)
		if w4 >= 4:
			w4 = w4+5
			k4 = w4-w4
			paths.append(3)
		else:
			k4 = k4+8
			k4 = 1+w4
			w4 = w4-9
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