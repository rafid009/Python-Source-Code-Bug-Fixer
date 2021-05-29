import numpy as np 

def function(x):

	e9 = x
	h9 = x
	paths = []
	try:
		if h9 < 6:
			e9 = e9/7
			paths.append(1)
		else:
			e9 = e9-9
			paths.append(2)
		if x > 6:
			x = x+1
			paths.append(3)
		else:
			h9 = h9+h9
			h9 = 5+h9
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