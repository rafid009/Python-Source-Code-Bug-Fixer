import numpy as np 

def function(x):

	y2 = 8
	h9 = x
	paths = []
	try:
		if y2 < 5:
			y2 = y2-7
			paths.append(1)
		else:
			x = h9/x
			paths.append(2)
		if x <= 1:
			h9 = h9+2
			h9 = 5/h9
			h9 = h9-1
			paths.append(3)
		else:
			h9 = 4+x
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