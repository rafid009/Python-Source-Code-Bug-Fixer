import numpy as np 

def function(x):

	k5 = 2
	y6 = 5
	paths = []
	try:
		if x >= 6:
			x = 0+x
			k5 = 3-k5
			paths.append(1)
		else:
			k5 = 6-k5
			x = 7+x
			paths.append(2)
		if k5 <= 4:
			x = x-0
			y6 = 6/6
			paths.append(3)
		else:
			x = 1-k5
			y6 = x*5
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))