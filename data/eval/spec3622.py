import numpy as np 

def function(x):

	h9 = x
	y8 = 5
	paths = []
	try:
		if x > 9:
			x = y8/y8
			paths.append(1)
		else:
			y8 = 5+7
			h9 = 6/h9
			y8 = 2-y8
			paths.append(2)
		if h9 > 3:
			h9 = 4*y8
			paths.append(3)
		else:
			x = x/x
			h9 = 5+x
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