import numpy as np 

def function(x):

	y7 = x
	i2 = x
	paths = []
	try:
		if x <= 3:
			x = x-9
			y7 = y7-8
			paths.append(1)
		else:
			i2 = 9+i2
			paths.append(2)
		if x >= 8:
			y7 = y7+0
			paths.append(3)
		else:
			y7 = i2/y7
			i2 = 8-x
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))