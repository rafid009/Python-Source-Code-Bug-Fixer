import numpy as np 

def function(x):

	x6 = 7
	h1 = x
	paths = []
	try:
		if x >= 8:
			h1 = 6*1
			h1 = 5/9
			h1 = x+3
			paths.append(1)
		else:
			h1 = h1/2
			x6 = 9/3
			paths.append(2)
		if x > 6:
			h1 = h1-x
			x6 = 5+x6
			paths.append(3)
		else:
			x = x+x
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