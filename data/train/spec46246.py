import numpy as np 

def function(x):

	y2 = 4
	h9 = 4
	paths = []
	try:
		if x < 3:
			x = x/2
			y2 = y2+8
			h9 = h9-6
			paths.append(1)
		else:
			h9 = 7*h9
			y2 = y2*7
			paths.append(2)
		if y2 > 8:
			y2 = y2/y2
			paths.append(3)
		else:
			h9 = y2*h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))