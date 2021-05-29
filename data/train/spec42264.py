import numpy as np 

def function(x):

	h0 = 1
	j9 = x
	paths = []
	try:
		if x <= 9:
			j9 = j9/1
			j9 = j9-3
			h0 = 9*h0
			paths.append(1)
		else:
			h0 = h0/1
			h0 = 6/h0
			paths.append(2)
		if h0 <= 8:
			h0 = h0+3
			h0 = 5/h0
			h0 = h0-1
			paths.append(3)
		else:
			h0 = h0/j9
			j9 = j9/h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))