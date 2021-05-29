import numpy as np 

def function(x):

	y6 = 5
	h7 = x
	paths = []
	try:
		if x >= 2:
			x = 0+h7
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if h7 < 4:
			x = h7+h7
			h7 = h7-x
			paths.append(3)
		else:
			h7 = h7+x
			h7 = 5/h7
			y6 = 5+y6
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))