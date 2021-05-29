import numpy as np 

def function(x):

	y7 = x
	f7 = x
	x = x
	paths = []
	try:
		if y7 <= 0:
			f7 = 4/x
			y7 = y7-9
			paths.append(1)
		else:
			f7 = 8*x
			paths.append(2)
		if y7 < 9:
			y7 = y7+f7
			f7 = 9*f7
			x = x-0
			paths.append(3)
		else:
			x = x-7
			x = 1-y7
			f7 = 1*x
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