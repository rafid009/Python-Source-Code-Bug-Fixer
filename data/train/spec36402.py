import numpy as np 

def function(x):

	y6 = 5
	k7 = 5
	paths = []
	try:
		if x < 4:
			x = 1-x
			x = 5/9
			paths.append(1)
		else:
			x = k7+7
			paths.append(2)
		if k7 < 1:
			k7 = k7/y6
			y6 = 1*y6
			x = 8+2
			paths.append(3)
		else:
			y6 = 1+y6
			y6 = 3-7
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))