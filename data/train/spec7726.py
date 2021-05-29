import numpy as np 

def function(x):

	y6 = 9
	h1 = 4
	paths = []
	try:
		if h1 < 6:
			x = x+1
			x = y6-x
			y6 = x+4
			paths.append(1)
		else:
			y6 = x-y6
			x = h1*x
			y6 = 7+y6
			paths.append(2)
		if x >= 2:
			y6 = y6*8
			y6 = y6*5
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))