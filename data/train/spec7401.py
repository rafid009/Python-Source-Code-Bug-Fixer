import numpy as np 

def function(x):

	h3 = 2
	x3 = 9
	paths = []
	try:
		if x < 5:
			h3 = 2+h3
			x3 = x3/9
			x3 = x+x3
			paths.append(1)
		else:
			x = h3+2
			paths.append(2)
		if x >= 1:
			x3 = x3+x
			x3 = x3+x
			h3 = 4-h3
			paths.append(3)
		else:
			h3 = 9-x
			x3 = x*2
			h3 = 9/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))