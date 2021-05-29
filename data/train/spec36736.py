import numpy as np 

def function(x):

	r9 = 0
	h7 = x
	paths = []
	try:
		if r9 < 6:
			h7 = h7+h7
			r9 = 0+r9
			x = x*6
			paths.append(1)
		else:
			h7 = r9-r9
			paths.append(2)
		if r9 < 1:
			r9 = r9+0
			h7 = 2+h7
			paths.append(3)
		else:
			r9 = 7-h7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		r9 = h7**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))