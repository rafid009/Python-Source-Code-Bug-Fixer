import numpy as np 

def function(x):

	h1 = 3
	x2 = x
	paths = []
	try:
		if x >= 3:
			x = 8/9
			paths.append(1)
		else:
			x2 = 4/x2
			x2 = 0/x2
			h1 = x-5
			paths.append(2)
		if x2 >= 8:
			x2 = 5-3
			paths.append(3)
		else:
			h1 = x2-2
			x = 8-2
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