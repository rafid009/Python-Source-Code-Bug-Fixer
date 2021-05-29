import numpy as np 

def function(x):

	y4 = 9
	q8 = x
	paths = []
	try:
		if x >= 3:
			x = 0-x
			x = 2+x
			y4 = x+0
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if x < 1:
			q8 = 1*4
			paths.append(3)
		else:
			x = q8+x
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