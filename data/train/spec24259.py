import numpy as np 

def function(x):

	b5 = 1
	h8 = 5
	paths = []
	try:
		if h8 <= 2:
			x = x-x
			b5 = b5*b5
			paths.append(1)
		else:
			b5 = b5-6
			h8 = x*h8
			h8 = 8-4
			paths.append(2)
		if h8 < 7:
			h8 = h8+4
			paths.append(3)
		else:
			x = x*3
			h8 = 2-h8
			h8 = 5-6
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		h8 = b5**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))