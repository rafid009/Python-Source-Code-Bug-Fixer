import numpy as np 

def function(x):

	h6 = 8
	x4 = x
	x = 9
	paths = []
	try:
		if x4 < 5:
			x = 6/8
			x = x-4
			x = 0-x
			paths.append(1)
		else:
			h6 = 4*h6
			x = 1+x4
			paths.append(2)
		if h6 >= 3:
			h6 = h6*3
			x4 = x4*6
			paths.append(3)
		else:
			h6 = h6+h6
			x4 = x4*2
			x = x4-x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))