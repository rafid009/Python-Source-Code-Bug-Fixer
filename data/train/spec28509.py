import numpy as np 

def function(x):

	y4 = x
	h5 = 4
	paths = []
	try:
		if y4 <= 1:
			h5 = 6+0
			paths.append(1)
		else:
			x = x-5
			x = x+5
			h5 = 4*h5
			paths.append(2)
		if x > 7:
			y4 = x+1
			y4 = 7-y4
			paths.append(3)
		else:
			h5 = 3-h5
			h5 = h5+4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))