import numpy as np 

def function(x):

	x0 = 2
	n7 = 9
	x = x
	paths = []
	try:
		if n7 < 8:
			x0 = x0-x0
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if x <= 5:
			x0 = x0-4
			n7 = x-5
			x0 = x0+n7
			paths.append(3)
		else:
			x0 = x0*3
			n7 = n7*4
			n7 = n7/1
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x0 = n7**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))