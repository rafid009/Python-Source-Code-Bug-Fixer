import numpy as np 

def function(x):

	h8 = x
	a4 = 6
	paths = []
	try:
		if h8 >= 9:
			h8 = 3/h8
			a4 = h8/a4
			paths.append(1)
		else:
			x = a4-8
			a4 = h8+h8
			paths.append(2)
		if h8 > 9:
			x = x*h8
			h8 = x-h8
			x = x-8
			paths.append(3)
		else:
			h8 = a4+5
			h8 = h8/1
			x = 1+6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))