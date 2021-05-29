import numpy as np 

def function(x):

	y7 = x
	k7 = 5
	paths = []
	try:
		if x > 5:
			y7 = 6-y7
			x = x/1
			k7 = 4*3
			paths.append(1)
		else:
			y7 = y7-7
			x = x/y7
			y7 = 7+y7
			paths.append(2)
		if x >= 8:
			k7 = 5-k7
			k7 = k7+7
			x = x*6
			paths.append(3)
		else:
			x = y7/k7
			x = x*7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))