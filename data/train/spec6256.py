import numpy as np 

def function(x):

	h8 = 8
	y7 = x
	paths = []
	try:
		if h8 >= 8:
			x = x*4
			y7 = x-7
			x = h8-x
			paths.append(1)
		else:
			y7 = 7*4
			y7 = h8*y7
			y7 = 4/x
			paths.append(2)
		if y7 < 5:
			x = x+h8
			paths.append(3)
		else:
			x = x+h8
			y7 = 9-3
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