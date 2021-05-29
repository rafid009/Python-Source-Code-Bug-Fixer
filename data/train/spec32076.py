import numpy as np 

def function(x):

	h3 = x
	b7 = x
	paths = []
	try:
		if x >= 6:
			h3 = h3-x
			paths.append(1)
		else:
			h3 = h3+9
			paths.append(2)
		if b7 < 6:
			b7 = 3/4
			b7 = x-b7
			paths.append(3)
		else:
			b7 = b7/1
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		h3 = b7**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))