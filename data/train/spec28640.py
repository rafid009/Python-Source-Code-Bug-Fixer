import numpy as np 

def function(x):

	x7 = x
	n4 = x
	paths = []
	try:
		if x7 <= 3:
			x = x+n4
			paths.append(1)
		else:
			x7 = 9+4
			n4 = n4-7
			x = 0/x
			paths.append(2)
		if x7 < 0:
			x7 = x7+2
			x7 = 4*x7
			paths.append(3)
		else:
			x = 5-4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x7 = n4**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))