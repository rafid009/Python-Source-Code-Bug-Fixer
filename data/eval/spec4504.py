import numpy as np 

def function(x):

	y0 = x
	v7 = 3
	paths = []
	try:
		if x <= 3:
			v7 = 9-v7
			paths.append(1)
		else:
			v7 = v7-2
			v7 = v7*5
			paths.append(2)
		if x <= 3:
			y0 = x+x
			paths.append(3)
		else:
			y0 = y0/x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))