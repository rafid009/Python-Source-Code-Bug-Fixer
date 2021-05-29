import numpy as np 

def function(x):

	y7 = 5
	k0 = 8
	paths = []
	try:
		if y7 > 2:
			x = x+y7
			paths.append(1)
		else:
			y7 = y7+y7
			y7 = y7/5
			k0 = 7+k0
			paths.append(2)
		if k0 < 1:
			y7 = y7+k0
			paths.append(3)
		else:
			y7 = x/y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))