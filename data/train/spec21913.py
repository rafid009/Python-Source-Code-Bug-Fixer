import numpy as np 

def function(x):

	v7 = 5
	y0 = 6
	paths = []
	try:
		if v7 < 6:
			v7 = 3-v7
			paths.append(1)
		else:
			y0 = y0-8
			paths.append(2)
		if v7 >= 0:
			x = v7+2
			y0 = y0+9
			y0 = 5+4
			paths.append(3)
		else:
			y0 = y0/v7
			v7 = 9*v7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))