import numpy as np 

def function(x):

	y1 = 4
	w4 = 8
	paths = []
	try:
		if w4 <= 6:
			x = x-3
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if x < 9:
			w4 = w4+5
			w4 = x/3
			paths.append(3)
		else:
			y1 = 9+0
			w4 = w4/y1
			w4 = 9/x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))