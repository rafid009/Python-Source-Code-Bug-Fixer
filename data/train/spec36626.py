import numpy as np 

def function(x):

	h1 = x
	y7 = 1
	x = x
	paths = []
	try:
		if x > 5:
			h1 = h1-x
			h1 = 4/3
			paths.append(1)
		else:
			y7 = y7-2
			h1 = h1-x
			paths.append(2)
		if y7 <= 6:
			x = 0+x
			paths.append(3)
		else:
			x = h1+y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))