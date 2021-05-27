import numpy as np 

def function(x):

	h9 = 6
	y1 = x
	paths = []
	try:
		if h9 > 4:
			h9 = 4+9
			paths.append(1)
		else:
			h9 = h9+y1
			h9 = 2/9
			paths.append(2)
		if x < 5:
			y1 = y1+y1
			y1 = y1-9
			paths.append(3)
		else:
			x = 8-x
			h9 = h9+6
			y1 = 5+4
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))