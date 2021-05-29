import numpy as np 

def function(x):

	x8 = 9
	n5 = x
	paths = []
	try:
		if x >= 6:
			n5 = 7-0
			paths.append(1)
		else:
			n5 = 4-x
			x = 7+8
			paths.append(2)
		if x >= 5:
			x = 8/x
			x = 3+x
			x = 8*x
			paths.append(3)
		else:
			x8 = x8*x
			x8 = n5-n5
			x8 = 8+x8
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))