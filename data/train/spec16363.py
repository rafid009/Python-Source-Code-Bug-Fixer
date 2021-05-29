import numpy as np 

def function(x):

	x6 = x
	h8 = x
	paths = []
	try:
		if x6 <= 3:
			h8 = 7/h8
			paths.append(1)
		else:
			x = h8-1
			h8 = h8-3
			paths.append(2)
		if h8 >= 5:
			h8 = x*h8
			x = 5*6
			x6 = x6-7
			paths.append(3)
		else:
			h8 = 2/h8
			x = x6/1
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))