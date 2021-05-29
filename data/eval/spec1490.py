import numpy as np 

def function(x):

	e9 = 2
	k7 = 8
	paths = []
	try:
		if k7 >= 8:
			k7 = 5-k7
			x = x-8
			paths.append(1)
		else:
			k7 = k7-6
			paths.append(2)
		if x > 5:
			x = 7/e9
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))