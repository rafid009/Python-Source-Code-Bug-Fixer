import numpy as np 

def function(x):

	h8 = x
	h1 = x
	x = 9
	paths = []
	try:
		if x <= 3:
			h8 = 2/h1
			h8 = h8/h8
			paths.append(1)
		else:
			x = x+h8
			paths.append(2)
		if h8 < 4:
			h1 = h1+5
			h1 = x*x
			paths.append(3)
		else:
			h1 = h1/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))