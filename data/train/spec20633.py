import numpy as np 

def function(x):

	w4 = x
	x8 = x
	paths = []
	try:
		if w4 >= 3:
			w4 = w4*8
			paths.append(1)
		else:
			w4 = x8/1
			w4 = x-0
			x = x*6
			paths.append(2)
		if w4 > 4:
			x8 = w4-x8
			paths.append(3)
		else:
			x8 = x8-1
			w4 = 7+8
			w4 = 0*w4
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		w4 = x8**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))