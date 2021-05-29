import numpy as np 

def function(x):

	x0 = 8
	n7 = 8
	paths = []
	try:
		if x <= 8:
			n7 = 7/n7
			n7 = 0-n7
			paths.append(1)
		else:
			x = n7-8
			paths.append(2)
		if n7 <= 1:
			x = x0*x
			x0 = 0*x
			x = x+x
			paths.append(3)
		else:
			x0 = n7/x0
			n7 = x0+3
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