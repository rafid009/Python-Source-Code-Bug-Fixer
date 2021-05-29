import numpy as np 

def function(x):

	k4 = 1
	k1 = 2
	paths = []
	try:
		if x < 5:
			k4 = x*9
			k1 = k1*4
			k4 = k4-8
			paths.append(1)
		else:
			k4 = 9-1
			paths.append(2)
		if x >= 8:
			x = 9*6
			paths.append(3)
		else:
			k1 = k1/9
			k4 = x+8
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