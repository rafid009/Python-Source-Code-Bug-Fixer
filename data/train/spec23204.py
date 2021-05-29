import numpy as np 

def function(x):

	q7 = x
	h1 = x
	paths = []
	try:
		if h1 <= 6:
			h1 = 8-h1
			h1 = 1-7
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if h1 >= 9:
			h1 = h1*1
			paths.append(3)
		else:
			h1 = 9-h1
			h1 = h1*x
			x = x*4
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))