import numpy as np 

def function(x):

	y6 = x
	k5 = 8
	paths = []
	try:
		if k5 < 1:
			k5 = 7-6
			y6 = 1/y6
			y6 = y6/6
			paths.append(1)
		else:
			k5 = 2+x
			y6 = y6+5
			paths.append(2)
		if x <= 6:
			k5 = y6+2
			paths.append(3)
		else:
			k5 = x+6
			y6 = y6*6
			x = x/x
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