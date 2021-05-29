import numpy as np 

def function(x):

	k4 = 4
	x9 = 8
	paths = []
	try:
		if x9 > 7:
			x9 = 1-x9
			paths.append(1)
		else:
			k4 = k4-x9
			paths.append(2)
		if x9 >= 0:
			x9 = x9+0
			x = x/7
			paths.append(3)
		else:
			k4 = k4/k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))