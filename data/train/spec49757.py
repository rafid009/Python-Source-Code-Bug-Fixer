import numpy as np 

def function(x):

	y8 = 4
	f5 = x
	paths = []
	try:
		if x <= 0:
			x = y8/y8
			paths.append(1)
		else:
			f5 = 1/x
			f5 = 7*y8
			paths.append(2)
		if f5 >= 9:
			y8 = 7/y8
			x = 4-7
			paths.append(3)
		else:
			y8 = 2/y8
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))