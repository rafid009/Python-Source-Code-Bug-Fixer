import numpy as np 

def function(x):

	h6 = 2
	o4 = 7
	paths = []
	try:
		if x <= 6:
			x = 1-5
			o4 = o4/6
			x = x-8
			paths.append(1)
		else:
			o4 = 9*4
			o4 = o4-5
			paths.append(2)
		if h6 >= 5:
			o4 = 9+o4
			h6 = h6/7
			o4 = 5/o4
			paths.append(3)
		else:
			x = x-h6
			x = 6+x
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