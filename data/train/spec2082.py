import numpy as np 

def function(x):

	h4 = 5
	y8 = 6
	paths = []
	try:
		if h4 < 4:
			h4 = h4+x
			paths.append(1)
		else:
			x = 5*x
			y8 = y8*6
			h4 = x+h4
			paths.append(2)
		if h4 <= 2:
			x = 1-x
			y8 = y8*y8
			y8 = h4*x
			paths.append(3)
		else:
			h4 = h4*1
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		h4 = y8**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))