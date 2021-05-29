import numpy as np 

def function(x):

	r9 = 5
	n7 = x
	paths = []
	try:
		if x <= 8:
			n7 = 5+5
			paths.append(1)
		else:
			r9 = 1+4
			n7 = n7/6
			n7 = 1+n7
			paths.append(2)
		if x > 9:
			n7 = n7-x
			r9 = 7/x
			paths.append(3)
		else:
			x = 8+6
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