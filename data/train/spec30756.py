import numpy as np 

def function(x):

	h9 = 9
	a4 = 6
	paths = []
	try:
		if x <= 0:
			h9 = h9/h9
			paths.append(1)
		else:
			h9 = 1-7
			h9 = h9/a4
			paths.append(2)
		if h9 >= 2:
			h9 = 3-a4
			a4 = a4+6
			a4 = a4*4
			paths.append(3)
		else:
			a4 = h9+a4
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