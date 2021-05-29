import numpy as np 

def function(x):

	y6 = x
	h7 = 3
	paths = []
	try:
		if h7 > 6:
			h7 = h7+x
			x = x*5
			y6 = h7*y6
			paths.append(1)
		else:
			h7 = 4+3
			x = x-6
			paths.append(2)
		if x > 7:
			y6 = x/h7
			x = h7+8
			paths.append(3)
		else:
			x = h7*y6
			x = h7/x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))