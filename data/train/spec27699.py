import numpy as np 

def function(x):

	x6 = x
	k4 = 8
	paths = []
	try:
		if x6 > 0:
			x = 1+x6
			x = 3+2
			k4 = 5-0
			paths.append(1)
		else:
			k4 = 5+2
			paths.append(2)
		if x6 > 2:
			k4 = 8-k4
			x6 = k4-x6
			paths.append(3)
		else:
			x6 = x6+8
			x6 = k4-7
			x6 = x-x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))