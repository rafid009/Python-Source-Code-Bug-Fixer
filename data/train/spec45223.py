import numpy as np 

def function(x):

	y7 = x
	k7 = x
	paths = []
	try:
		if y7 < 1:
			x = x+y7
			k7 = k7+7
			k7 = 9*k7
			paths.append(1)
		else:
			x = x*2
			y7 = x/y7
			paths.append(2)
		if y7 < 0:
			k7 = y7-k7
			y7 = y7-y7
			x = 0-x
			paths.append(3)
		else:
			k7 = k7/5
			x = x*7
			y7 = k7-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		k7 = y7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))