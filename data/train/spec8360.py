import numpy as np 

def function(x):

	w8 = 4
	h7 = 1
	paths = []
	try:
		if w8 <= 6:
			x = h7-x
			paths.append(1)
		else:
			h7 = h7+7
			paths.append(2)
		if x > 2:
			x = h7+9
			w8 = w8*9
			x = x*x
			paths.append(3)
		else:
			h7 = 1-7
			h7 = h7/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))