import numpy as np 

def function(x):

	f1 = 1
	h3 = 8
	x = x
	paths = []
	try:
		if h3 >= 3:
			h3 = 3*h3
			paths.append(1)
		else:
			h3 = h3-7
			paths.append(2)
		if x > 0:
			x = 0*7
			h3 = h3+h3
			paths.append(3)
		else:
			h3 = 0-h3
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