import numpy as np 

def function(x):

	w2 = 4
	h8 = 0
	paths = []
	try:
		if x >= 9:
			x = 3/6
			w2 = w2-8
			x = 6-2
			paths.append(1)
		else:
			h8 = h8*4
			paths.append(2)
		if h8 < 1:
			h8 = w2-8
			paths.append(3)
		else:
			x = x+8
			w2 = x/h8
			x = 6+0
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		h8 = w2**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))