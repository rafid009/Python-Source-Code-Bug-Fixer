import numpy as np 

def function(x):

	y5 = 7
	h3 = x
	paths = []
	try:
		if h3 <= 3:
			x = x+8
			x = x-6
			paths.append(1)
		else:
			x = 5-3
			paths.append(2)
		if h3 >= 8:
			h3 = h3-h3
			h3 = 5+0
			paths.append(3)
		else:
			h3 = 7/h3
			y5 = x/x
			y5 = y5*x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))