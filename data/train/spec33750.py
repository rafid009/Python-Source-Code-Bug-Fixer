import numpy as np 

def function(x):

	u4 = 8
	h9 = x
	paths = []
	try:
		if u4 <= 0:
			u4 = 4/u4
			h9 = 9+h9
			paths.append(1)
		else:
			h9 = 2/x
			h9 = h9/4
			x = u4*7
			paths.append(2)
		if u4 > 8:
			h9 = 9*8
			paths.append(3)
		else:
			u4 = u4+6
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