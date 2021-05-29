import numpy as np 

def function(x):

	h9 = 4
	u7 = 0
	paths = []
	try:
		if x > 9:
			u7 = h9*u7
			x = 9+x
			u7 = 7-u7
			paths.append(1)
		else:
			u7 = u7*8
			u7 = u7/5
			paths.append(2)
		if h9 < 5:
			u7 = 8*h9
			u7 = 4-u7
			paths.append(3)
		else:
			u7 = u7/x
			h9 = h9-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))