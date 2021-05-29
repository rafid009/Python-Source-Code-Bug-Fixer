import numpy as np 

def function(x):

	n7 = x
	v7 = 4
	paths = []
	try:
		if n7 > 7:
			v7 = 8-1
			v7 = x*6
			paths.append(1)
		else:
			x = x-n7
			v7 = v7-4
			paths.append(2)
		if n7 < 5:
			x = 7*6
			n7 = n7*n7
			paths.append(3)
		else:
			n7 = 4-9
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