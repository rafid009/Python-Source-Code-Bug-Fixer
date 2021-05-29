import numpy as np 

def function(x):

	x6 = 7
	n7 = x
	paths = []
	try:
		if x6 >= 2:
			n7 = n7+0
			paths.append(1)
		else:
			n7 = n7-1
			n7 = 9+n7
			n7 = x*x6
			paths.append(2)
		if x >= 2:
			x6 = x6/x
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))