import numpy as np 

def function(x):

	y7 = 3
	h8 = x
	paths = []
	try:
		if y7 > 1:
			y7 = y7*7
			h8 = h8*7
			paths.append(1)
		else:
			y7 = 7/y7
			h8 = h8/x
			y7 = y7*4
			paths.append(2)
		if h8 < 0:
			y7 = h8/8
			h8 = h8/9
			x = 2+h8
			paths.append(3)
		else:
			h8 = h8*9
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		y7 = h8**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))