import numpy as np 

def function(x):

	h1 = 2
	e7 = x
	paths = []
	try:
		if e7 < 3:
			h1 = h1-1
			h1 = e7*h1
			paths.append(1)
		else:
			e7 = 0/x
			paths.append(2)
		if e7 < 0:
			x = x+6
			h1 = 4/h1
			paths.append(3)
		else:
			h1 = 6/5
			e7 = 0-3
			e7 = 1/e7
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