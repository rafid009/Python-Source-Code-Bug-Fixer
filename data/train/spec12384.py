import numpy as np 

def function(x):

	k2 = 5
	h6 = 8
	x = x
	paths = []
	try:
		if k2 > 8:
			k2 = 4+5
			paths.append(1)
		else:
			k2 = 3-k2
			paths.append(2)
		if k2 > 0:
			x = 8/x
			h6 = h6-8
			x = 4-3
			paths.append(3)
		else:
			h6 = h6*k2
			h6 = h6+8
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))