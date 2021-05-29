import numpy as np 

def function(x):

	h6 = 8
	z7 = x
	paths = []
	try:
		if z7 > 5:
			h6 = 7/x
			x = z7*h6
			x = 3/6
			paths.append(1)
		else:
			h6 = 6*h6
			paths.append(2)
		if x < 1:
			x = h6-4
			paths.append(3)
		else:
			x = z7/x
			x = 7*z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))