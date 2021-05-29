import numpy as np 

def function(x):

	y7 = 4
	n7 = 5
	x = x
	paths = []
	try:
		if y7 < 2:
			x = 5-3
			n7 = 6*n7
			paths.append(1)
		else:
			n7 = n7*0
			y7 = 9-y7
			paths.append(2)
		if y7 < 9:
			n7 = n7-y7
			y7 = y7-y7
			paths.append(3)
		else:
			x = 6*n7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))