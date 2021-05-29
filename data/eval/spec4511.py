import numpy as np 

def function(x):

	x9 = x
	x4 = x
	paths = []
	try:
		if x4 > 8:
			x = x-0
			paths.append(1)
		else:
			x9 = 7/x9
			paths.append(2)
		if x9 <= 9:
			x9 = x9+6
			paths.append(3)
		else:
			x = x4+3
			x4 = 0/5
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))