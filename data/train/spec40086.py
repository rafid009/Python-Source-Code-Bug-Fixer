import numpy as np 

def function(x):

	h9 = x
	i6 = 0
	paths = []
	try:
		if x < 1:
			x = x+3
			h9 = 8*h9
			i6 = h9*h9
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if h9 >= 7:
			x = 2+x
			h9 = h9-i6
			x = x/3
			paths.append(3)
		else:
			h9 = 6-h9
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