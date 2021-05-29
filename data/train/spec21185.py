import numpy as np 

def function(x):

	k2 = 8
	x9 = 2
	paths = []
	try:
		if x9 > 7:
			x = 1-x
			paths.append(1)
		else:
			k2 = k2+7
			paths.append(2)
		if k2 > 7:
			x = 8*x
			x9 = x9-4
			paths.append(3)
		else:
			x = x9*3
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))