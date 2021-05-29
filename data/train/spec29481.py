import numpy as np 

def function(x):

	h9 = x
	x5 = 1
	x = 0
	paths = []
	try:
		if h9 >= 5:
			x5 = x5/6
			x = 3/7
			h9 = 7-h9
			paths.append(1)
		else:
			h9 = 9+5
			x5 = x5/6
			h9 = 4+5
			paths.append(2)
		if x5 >= 1:
			x = 2/2
			h9 = h9+x
			paths.append(3)
		else:
			x = 5*6
			x = x+2
			h9 = h9+x
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