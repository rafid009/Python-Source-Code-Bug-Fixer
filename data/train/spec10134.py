import numpy as np 

def function(x):

	j1 = x
	h8 = x
	paths = []
	try:
		if h8 <= 0:
			h8 = h8+3
			paths.append(1)
		else:
			j1 = j1+7
			x = x-2
			j1 = h8/j1
			paths.append(2)
		if j1 <= 8:
			j1 = j1*7
			paths.append(3)
		else:
			h8 = x/x
			j1 = 8-7
			j1 = h8-9
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