import numpy as np 

def function(x):

	x8 = 8
	x5 = 5
	paths = []
	try:
		if x5 >= 0:
			x8 = 5/x
			x5 = x-x5
			x5 = x5*7
			paths.append(1)
		else:
			x5 = 2+x5
			paths.append(2)
		if x > 3:
			x8 = x8/7
			x = 3/2
			x = x5+x8
			paths.append(3)
		else:
			x5 = 8/x5
			x5 = 5-3
			x8 = x8+x8
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x8 = x5**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))