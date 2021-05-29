import numpy as np 

def function(x):

	p2 = 1
	h8 = 9
	paths = []
	try:
		if h8 < 9:
			h8 = 3*1
			h8 = h8*8
			h8 = 8+1
			paths.append(1)
		else:
			h8 = 2/h8
			h8 = p2+h8
			paths.append(2)
		if h8 <= 5:
			p2 = p2/h8
			p2 = p2+8
			h8 = 9+2
			paths.append(3)
		else:
			h8 = h8/2
			p2 = 3+x
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