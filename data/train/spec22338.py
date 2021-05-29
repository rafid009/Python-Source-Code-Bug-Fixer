import numpy as np 

def function(x):

	y8 = 5
	e0 = x
	paths = []
	try:
		if y8 <= 9:
			y8 = e0+y8
			y8 = 9+3
			y8 = y8-9
			paths.append(1)
		else:
			e0 = e0+8
			x = 0*x
			y8 = 7+y8
			paths.append(2)
		if x > 6:
			y8 = e0*y8
			paths.append(3)
		else:
			y8 = y8-x
			y8 = e0-y8
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