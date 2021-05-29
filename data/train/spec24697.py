import numpy as np 

def function(x):

	k2 = 0
	h6 = x
	paths = []
	try:
		if h6 <= 5:
			k2 = x-1
			k2 = k2*h6
			paths.append(1)
		else:
			k2 = k2+7
			x = 1+x
			h6 = 0-h6
			paths.append(2)
		if x >= 9:
			k2 = k2*9
			k2 = h6-x
			x = x-6
			paths.append(3)
		else:
			h6 = h6*h6
			k2 = k2+x
			k2 = 6+x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))