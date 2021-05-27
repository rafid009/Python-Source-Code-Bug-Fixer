import numpy as np 

def function(x):

	n9 = 3
	n7 = x
	paths = []
	try:
		if x < 4:
			x = 4/6
			x = 5-3
			n9 = n9*n7
			paths.append(1)
		else:
			n7 = n7/8
			n7 = n7*3
			paths.append(2)
		if n7 < 2:
			n9 = 8-8
			n9 = n9+2
			n9 = n9/n9
			paths.append(3)
		else:
			n7 = n9*9
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