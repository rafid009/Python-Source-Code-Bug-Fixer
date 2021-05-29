import numpy as np 

def function(x):

	a8 = 6
	h4 = x
	paths = []
	try:
		if h4 < 8:
			x = x+8
			x = x*a8
			paths.append(1)
		else:
			h4 = 5*h4
			a8 = 7/a8
			paths.append(2)
		if h4 >= 5:
			a8 = 9/a8
			x = 6/x
			paths.append(3)
		else:
			x = x-7
			a8 = x/h4
			a8 = 9-x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))