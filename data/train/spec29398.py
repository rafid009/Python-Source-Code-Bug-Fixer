import numpy as np 

def function(x):

	h8 = 1
	y4 = 8
	paths = []
	try:
		if y4 < 3:
			x = x-2
			paths.append(1)
		else:
			h8 = h8+y4
			h8 = 5-7
			paths.append(2)
		if x < 8:
			h8 = 8/h8
			x = x/6
			x = 2-3
			paths.append(3)
		else:
			x = x/1
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))