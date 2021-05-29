import numpy as np 

def function(x):

	i8 = 7
	n5 = x
	paths = []
	try:
		if x > 4:
			n5 = n5+2
			paths.append(1)
		else:
			n5 = 3+n5
			n5 = 1*n5
			paths.append(2)
		if n5 > 1:
			n5 = 4*x
			x = 1-x
			paths.append(3)
		else:
			i8 = 5/i8
			x = x-3
			n5 = n5/n5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		i8 = n5**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))