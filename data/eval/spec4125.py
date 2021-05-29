import numpy as np 

def function(x):

	h7 = 7
	x3 = x
	paths = []
	try:
		if x3 <= 5:
			x3 = h7*x3
			x3 = 3-x
			paths.append(1)
		else:
			h7 = 9+9
			x3 = x3+3
			paths.append(2)
		if x >= 3:
			x3 = x3*8
			h7 = h7-1
			paths.append(3)
		else:
			x3 = x3/h7
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