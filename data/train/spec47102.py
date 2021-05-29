import numpy as np 

def function(x):

	u7 = x
	h8 = 4
	paths = []
	try:
		if x >= 9:
			u7 = u7/x
			paths.append(1)
		else:
			u7 = u7+0
			x = 3/h8
			u7 = h8*u7
			paths.append(2)
		if h8 > 5:
			u7 = h8-u7
			paths.append(3)
		else:
			x = h8*u7
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