import numpy as np 

def function(x):

	h9 = x
	q4 = x
	paths = []
	try:
		if q4 > 9:
			h9 = 4/q4
			x = h9-4
			paths.append(1)
		else:
			q4 = 1-2
			x = x+6
			paths.append(2)
		if h9 > 3:
			h9 = 5*h9
			x = h9-4
			paths.append(3)
		else:
			x = 8*9
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