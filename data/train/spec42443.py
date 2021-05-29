import numpy as np 

def function(x):

	a8 = 7
	n4 = x
	paths = []
	try:
		if a8 >= 1:
			a8 = 9+a8
			n4 = n4-x
			a8 = a8*9
			paths.append(1)
		else:
			x = 5/x
			n4 = n4*4
			paths.append(2)
		if x < 8:
			a8 = a8*a8
			n4 = 4*3
			paths.append(3)
		else:
			n4 = 2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))