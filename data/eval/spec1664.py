import numpy as np 

def function(x):

	h6 = x
	k2 = x
	paths = []
	try:
		if k2 <= 5:
			h6 = 1-h6
			paths.append(1)
		else:
			k2 = 8/7
			h6 = h6*9
			x = x-7
			paths.append(2)
		if h6 > 5:
			h6 = 5/h6
			x = 0/k2
			h6 = h6*k2
			paths.append(3)
		else:
			h6 = k2-h6
			h6 = 5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))