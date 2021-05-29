import numpy as np 

def function(x):

	h6 = x
	y7 = x
	x = 6
	paths = []
	try:
		if h6 > 2:
			y7 = h6+0
			x = x-7
			h6 = h6-h6
			paths.append(1)
		else:
			y7 = 8*1
			x = 8*1
			h6 = y7+h6
			paths.append(2)
		if y7 < 9:
			y7 = 4*y7
			x = x+4
			x = x-x
			paths.append(3)
		else:
			y7 = y7/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))