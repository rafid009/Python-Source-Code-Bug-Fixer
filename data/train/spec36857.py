import numpy as np 

def function(x):

	y8 = x
	k5 = x
	paths = []
	try:
		if k5 < 4:
			y8 = y8/y8
			k5 = k5+k5
			paths.append(1)
		else:
			y8 = y8/k5
			paths.append(2)
		if x >= 4:
			y8 = y8/5
			y8 = y8-6
			y8 = y8/9
			paths.append(3)
		else:
			k5 = 6-2
			k5 = k5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))