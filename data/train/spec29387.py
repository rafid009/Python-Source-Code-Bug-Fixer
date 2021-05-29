import numpy as np 

def function(x):

	w2 = 3
	h9 = x
	paths = []
	try:
		if x <= 8:
			h9 = x+h9
			h9 = h9/7
			x = 9-x
			paths.append(1)
		else:
			x = x/2
			h9 = 0-h9
			paths.append(2)
		if x < 8:
			h9 = 3*h9
			paths.append(3)
		else:
			h9 = h9+2
			h9 = h9*w2
			x = 0-1
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))