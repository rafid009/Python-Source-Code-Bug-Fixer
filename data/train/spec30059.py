import numpy as np 

def function(x):

	i7 = x
	h6 = 2
	paths = []
	try:
		if i7 > 9:
			i7 = 0*i7
			paths.append(1)
		else:
			i7 = i7+3
			x = x+8
			paths.append(2)
		if x >= 1:
			h6 = h6-4
			i7 = 4+i7
			paths.append(3)
		else:
			i7 = 7+i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))