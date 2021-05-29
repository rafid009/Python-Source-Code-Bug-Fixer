import numpy as np 

def function(x):

	h6 = 5
	w4 = x
	paths = []
	try:
		if x >= 7:
			w4 = w4-1
			paths.append(1)
		else:
			w4 = 1*w4
			paths.append(2)
		if x >= 5:
			h6 = 3-1
			h6 = 2+4
			paths.append(3)
		else:
			w4 = 9*0
			w4 = w4-5
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))