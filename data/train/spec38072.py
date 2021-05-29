import numpy as np 

def function(x):

	b7 = x
	y0 = x
	x = 1
	paths = []
	try:
		if b7 <= 5:
			b7 = b7*6
			b7 = 4-b7
			paths.append(1)
		else:
			x = 7-x
			x = 5-x
			y0 = y0/b7
			paths.append(2)
		if b7 < 3:
			x = x-4
			b7 = x*b7
			x = 2/x
			paths.append(3)
		else:
			b7 = 1-x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		y0 = b7**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))