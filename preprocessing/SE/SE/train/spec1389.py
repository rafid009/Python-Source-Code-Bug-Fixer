import numpy as np 

def function(x):

	y1 = 5
	y8 = 8
	paths = []
	try:
		if y8 > 5:
			y8 = y8-9
			x = 5+x
			paths.append(1)
		else:
			y1 = 3/y8
			paths.append(2)
		if y8 < 5:
			y8 = y8*3
			paths.append(3)
		else:
			y8 = y8-1
			y1 = y8-y1
			x = x*y1
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))