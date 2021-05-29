import numpy as np 

def function(x):

	a5 = 3
	x3 = 3
	paths = []
	try:
		if x >= 8:
			x = 8/x
			x3 = 0/x3
			paths.append(1)
		else:
			x3 = 0+x
			paths.append(2)
		if a5 < 3:
			x3 = 5-x3
			a5 = 4*x3
			paths.append(3)
		else:
			a5 = a5+8
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))