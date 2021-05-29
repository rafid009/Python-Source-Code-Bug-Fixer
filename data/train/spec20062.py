import numpy as np 

def function(x):

	o3 = 8
	n7 = 4
	paths = []
	try:
		if x <= 2:
			x = 6*x
			n7 = 4-n7
			paths.append(1)
		else:
			n7 = n7*3
			o3 = o3*9
			paths.append(2)
		if o3 <= 6:
			n7 = 3+o3
			paths.append(3)
		else:
			n7 = 1-9
			x = 1/x
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