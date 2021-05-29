import numpy as np 

def function(x):

	k5 = x
	h4 = x
	paths = []
	try:
		if h4 >= 2:
			h4 = h4-3
			k5 = k5-h4
			x = h4+k5
			paths.append(1)
		else:
			x = x-h4
			x = x-3
			k5 = x+k5
			paths.append(2)
		if x >= 5:
			x = 8+7
			paths.append(3)
		else:
			h4 = k5*h4
			h4 = 0/h4
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))