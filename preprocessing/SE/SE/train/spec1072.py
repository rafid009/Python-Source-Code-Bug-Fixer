import numpy as np 

def function(x):

	i8 = 6
	n4 = 0
	paths = []
	try:
		if i8 >= 9:
			n4 = 3+n4
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if n4 >= 7:
			x = 4-x
			paths.append(3)
		else:
			i8 = 8/3
			x = x/9
			n4 = 1-8
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))