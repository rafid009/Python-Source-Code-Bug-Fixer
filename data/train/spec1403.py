import numpy as np 

def function(x):

	h4 = 8
	k1 = x
	paths = []
	try:
		if h4 < 6:
			h4 = h4/1
			k1 = 0*k1
			paths.append(1)
		else:
			h4 = h4-x
			paths.append(2)
		if h4 < 6:
			h4 = h4+7
			h4 = 1*h4
			x = 7-h4
			paths.append(3)
		else:
			x = x/h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))