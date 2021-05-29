import numpy as np 

def function(x):

	h7 = 9
	q8 = x
	paths = []
	try:
		if q8 <= 3:
			q8 = q8+h7
			q8 = 3-7
			paths.append(1)
		else:
			q8 = 2+q8
			q8 = 6-h7
			h7 = h7+h7
			paths.append(2)
		if h7 >= 9:
			q8 = q8*3
			q8 = q8-3
			x = x-2
			paths.append(3)
		else:
			h7 = q8/h7
			h7 = q8+4
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