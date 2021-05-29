import numpy as np 

def function(x):

	h4 = x
	a6 = 7
	paths = []
	try:
		if a6 <= 8:
			a6 = a6*x
			paths.append(1)
		else:
			a6 = 2*8
			paths.append(2)
		if h4 >= 7:
			x = x-6
			h4 = 2-h4
			x = 8-5
			paths.append(3)
		else:
			a6 = 0+4
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