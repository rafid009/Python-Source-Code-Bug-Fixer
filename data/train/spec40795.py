import numpy as np 

def function(x):

	x6 = x
	h7 = x
	paths = []
	try:
		if x > 9:
			h7 = h7+7
			paths.append(1)
		else:
			x = 4+8
			h7 = 9-x6
			x = x-5
			paths.append(2)
		if x6 <= 0:
			x6 = h7/6
			x = 7-8
			paths.append(3)
		else:
			x6 = 4*9
			h7 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))