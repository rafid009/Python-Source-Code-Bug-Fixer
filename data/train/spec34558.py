import numpy as np 

def function(x):

	y2 = x
	x9 = x
	paths = []
	try:
		if y2 < 3:
			x = 6/y2
			x9 = x9-x
			paths.append(1)
		else:
			x = x/7
			x9 = 3-x
			x = 2-x
			paths.append(2)
		if y2 >= 7:
			x9 = 0*2
			y2 = 8-y2
			paths.append(3)
		else:
			x9 = 7/x9
			x = x*x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))