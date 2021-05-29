import numpy as np 

def function(x):

	y7 = x
	h4 = 0
	paths = []
	try:
		if h4 >= 4:
			x = x+3
			paths.append(1)
		else:
			y7 = y7*2
			paths.append(2)
		if h4 < 0:
			x = h4*x
			y7 = x*y7
			y7 = y7-7
			paths.append(3)
		else:
			h4 = y7*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))