import numpy as np 

def function(x):

	w5 = 7
	h8 = 4
	paths = []
	try:
		if h8 <= 2:
			h8 = 8+h8
			h8 = 3*h8
			paths.append(1)
		else:
			x = x/w5
			w5 = w5+4
			paths.append(2)
		if h8 < 6:
			h8 = h8+9
			h8 = h8*w5
			x = w5/x
			paths.append(3)
		else:
			h8 = 4+7
			x = x+h8
			h8 = 8+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))