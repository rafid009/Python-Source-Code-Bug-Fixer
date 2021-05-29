import numpy as np 

def function(x):

	i1 = 1
	h0 = 9
	paths = []
	try:
		if i1 < 2:
			h0 = 4-x
			h0 = h0*2
			paths.append(1)
		else:
			h0 = 6-h0
			h0 = 3/h0
			paths.append(2)
		if h0 >= 1:
			h0 = 1-3
			x = x+8
			paths.append(3)
		else:
			i1 = i1*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))