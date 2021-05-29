import numpy as np 

def function(x):

	h7 = x
	i6 = x
	paths = []
	try:
		if x < 2:
			h7 = 3/x
			i6 = 9/i6
			h7 = 2*h7
			paths.append(1)
		else:
			i6 = i6/2
			i6 = h7+3
			x = x/1
			paths.append(2)
		if h7 > 8:
			h7 = h7+3
			paths.append(3)
		else:
			h7 = x/9
			i6 = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))