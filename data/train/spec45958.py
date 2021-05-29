import numpy as np 

def function(x):

	x7 = 0
	f7 = 4
	paths = []
	try:
		if x7 > 5:
			x = x-7
			x7 = x/x7
			x7 = 7/x7
			paths.append(1)
		else:
			x7 = 4-2
			f7 = 9*f7
			paths.append(2)
		if x7 < 4:
			f7 = 7*5
			paths.append(3)
		else:
			x7 = x7*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))