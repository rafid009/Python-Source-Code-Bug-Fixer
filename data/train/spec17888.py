import numpy as np 

def function(x):

	q8 = 5
	y4 = 2
	paths = []
	try:
		if x >= 7:
			q8 = 1-q8
			paths.append(1)
		else:
			y4 = 9-q8
			y4 = 3-y4
			y4 = x/y4
			paths.append(2)
		if x < 7:
			y4 = 4-y4
			paths.append(3)
		else:
			q8 = q8-5
			y4 = y4*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))