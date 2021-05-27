import numpy as np 

def function(x):

	y2 = x
	h6 = 9
	paths = []
	try:
		if x < 7:
			h6 = 7*h6
			paths.append(1)
		else:
			h6 = h6-0
			paths.append(2)
		if y2 <= 3:
			h6 = h6/x
			x = x+9
			paths.append(3)
		else:
			y2 = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))