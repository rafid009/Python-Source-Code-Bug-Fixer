import numpy as np 

def function(x):

	h6 = x
	i9 = 9
	paths = []
	try:
		if x < 0:
			x = x*x
			x = i9-x
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x < 5:
			i9 = i9+h6
			paths.append(3)
		else:
			h6 = h6*6
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