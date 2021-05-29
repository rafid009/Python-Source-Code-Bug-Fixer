import numpy as np 

def function(x):

	b0 = x
	h9 = x
	paths = []
	try:
		if h9 < 3:
			b0 = 8+b0
			h9 = h9+8
			h9 = h9*x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if b0 > 9:
			x = 7-7
			x = 9+x
			x = 2-x
			paths.append(3)
		else:
			b0 = 6/b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		h9 = b0**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))