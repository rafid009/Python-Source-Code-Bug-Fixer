import numpy as np 

def function(x):

	x8 = 3
	q3 = x
	paths = []
	try:
		if q3 <= 7:
			q3 = x8-7
			paths.append(1)
		else:
			x8 = 4-x
			x = 3-x
			paths.append(2)
		if x >= 2:
			q3 = q3-2
			paths.append(3)
		else:
			q3 = q3+x8
			x = 3+x
			x = 6/x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))