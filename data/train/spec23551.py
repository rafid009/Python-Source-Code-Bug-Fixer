import numpy as np 

def function(x):

	h7 = 4
	j4 = x
	paths = []
	try:
		if h7 < 5:
			j4 = 2*j4
			x = x-4
			h7 = 7*9
			paths.append(1)
		else:
			h7 = 0/6
			paths.append(2)
		if h7 < 0:
			j4 = 3*j4
			paths.append(3)
		else:
			j4 = j4/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))