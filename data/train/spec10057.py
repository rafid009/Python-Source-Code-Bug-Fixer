import numpy as np 

def function(x):

	h1 = 7
	h6 = 7
	paths = []
	try:
		if h1 > 2:
			h1 = x+0
			h1 = 4+4
			paths.append(1)
		else:
			h6 = 8/9
			h1 = h1*2
			paths.append(2)
		if x <= 2:
			h1 = h1/7
			h1 = h1+h1
			paths.append(3)
		else:
			x = 2/2
			x = 5/5
			h1 = 1/h1
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