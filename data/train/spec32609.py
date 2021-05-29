import numpy as np 

def function(x):

	e9 = 3
	h7 = 1
	paths = []
	try:
		if h7 < 3:
			h7 = e9-5
			x = 6-7
			paths.append(1)
		else:
			h7 = 7+1
			x = 3/8
			x = 4+x
			paths.append(2)
		if x < 4:
			h7 = 3-7
			paths.append(3)
		else:
			h7 = h7+h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))