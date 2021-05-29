import numpy as np 

def function(x):

	h8 = 9
	b2 = x
	paths = []
	try:
		if b2 <= 1:
			h8 = h8-h8
			h8 = h8+b2
			paths.append(1)
		else:
			b2 = b2-1
			h8 = 1-h8
			x = h8-h8
			paths.append(2)
		if h8 > 8:
			h8 = b2/9
			b2 = x*9
			h8 = h8/x
			paths.append(3)
		else:
			x = 6*9
			x = 4-b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))