import numpy as np 

def function(x):

	h3 = x
	x9 = x
	paths = []
	try:
		if h3 > 7:
			x9 = h3-x9
			x9 = x9+6
			paths.append(1)
		else:
			x = x9+x
			x = x*6
			x = 4*x
			paths.append(2)
		if x9 > 1:
			x9 = 6-x9
			paths.append(3)
		else:
			x = x-8
			x = 4-x
			x9 = 8+x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		h3 = x9**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))