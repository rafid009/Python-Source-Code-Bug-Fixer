import numpy as np 

def function(x):

	h6 = 6
	k4 = x
	paths = []
	try:
		if h6 <= 3:
			k4 = x/7
			x = x+3
			h6 = 1+h6
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if k4 < 2:
			k4 = k4*1
			x = 7/x
			h6 = 4*h6
			paths.append(3)
		else:
			h6 = h6*7
			h6 = 9+3
			h6 = 4*h6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))