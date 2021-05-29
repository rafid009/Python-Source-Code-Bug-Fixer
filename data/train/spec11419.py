import numpy as np 

def function(x):

	a1 = x
	q8 = x
	paths = []
	try:
		if x < 8:
			a1 = a1-x
			x = x-x
			q8 = q8/3
			paths.append(1)
		else:
			x = 6-1
			paths.append(2)
		if a1 < 3:
			q8 = q8-4
			a1 = 8*3
			paths.append(3)
		else:
			q8 = 9+7
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))