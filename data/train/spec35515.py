import numpy as np 

def function(x):

	q4 = 4
	x8 = x
	x = 0
	paths = []
	try:
		if x8 >= 5:
			q4 = 7/x8
			x8 = 0-x8
			paths.append(1)
		else:
			q4 = 3+x8
			paths.append(2)
		if x >= 0:
			x8 = x-6
			paths.append(3)
		else:
			x8 = x/x8
			q4 = q4+q4
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