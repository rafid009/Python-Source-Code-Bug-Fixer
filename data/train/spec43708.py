import numpy as np 

def function(x):

	x4 = 1
	q8 = 0
	x = 6
	paths = []
	try:
		if x4 >= 9:
			x = q8*6
			paths.append(1)
		else:
			x = x-5
			x = x4-x
			x = x/7
			paths.append(2)
		if q8 > 3:
			x = x4-7
			x = 9-x
			x4 = x*x4
			paths.append(3)
		else:
			x = x-8
			q8 = q8-1
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x4 = q8**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))