import numpy as np 

def function(x):

	y8 = 4
	h8 = 6
	paths = []
	try:
		if x <= 7:
			y8 = 5+9
			y8 = 8-y8
			paths.append(1)
		else:
			h8 = h8-2
			x = 3-x
			paths.append(2)
		if y8 < 9:
			x = x/8
			y8 = y8-4
			paths.append(3)
		else:
			h8 = 1/x
			h8 = 0*h8
			h8 = y8/h8
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