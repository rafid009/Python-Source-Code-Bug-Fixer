import numpy as np 

def function(x):

	h7 = 0
	y6 = 5
	paths = []
	try:
		if y6 > 0:
			h7 = h7+9
			paths.append(1)
		else:
			x = 0+0
			paths.append(2)
		if y6 < 9:
			y6 = y6*3
			y6 = 5+h7
			h7 = h7+h7
			paths.append(3)
		else:
			y6 = 2+9
			h7 = h7*x
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