import numpy as np 

def function(x):

	h5 = x
	u4 = 2
	paths = []
	try:
		if u4 <= 8:
			h5 = x/h5
			paths.append(1)
		else:
			h5 = 9*h5
			h5 = 7-h5
			h5 = u4/3
			paths.append(2)
		if x < 0:
			h5 = 5*9
			h5 = 4-u4
			h5 = 1/h5
			paths.append(3)
		else:
			h5 = h5-0
			h5 = h5*x
			x = 8*x
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