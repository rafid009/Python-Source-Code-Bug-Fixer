import numpy as np 

def function(x):

	z6 = x
	h7 = 4
	paths = []
	try:
		if h7 <= 7:
			h7 = 8/z6
			x = 9*x
			x = x+8
			paths.append(1)
		else:
			h7 = x-1
			x = x/h7
			paths.append(2)
		if z6 >= 5:
			z6 = h7/1
			paths.append(3)
		else:
			h7 = 5-6
			x = z6/x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		h7 = z6**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))