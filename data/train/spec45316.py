import numpy as np 

def function(x):

	x4 = 4
	x7 = x
	paths = []
	try:
		if x < 8:
			x7 = x4/1
			x4 = x/x7
			x4 = 5/8
			paths.append(1)
		else:
			x7 = x7-5
			x7 = 3-x4
			paths.append(2)
		if x7 <= 7:
			x4 = 9*x4
			paths.append(3)
		else:
			x4 = 8-x4
			x7 = x7/x4
			x = 4-x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x4 = x7**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))