import numpy as np 

def function(x):

	h6 = 1
	o4 = x
	paths = []
	try:
		if o4 < 4:
			h6 = 9/h6
			h6 = 3-o4
			paths.append(1)
		else:
			o4 = 0+o4
			paths.append(2)
		if h6 >= 8:
			x = 5+x
			paths.append(3)
		else:
			h6 = 0-h6
			h6 = 9+7
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))