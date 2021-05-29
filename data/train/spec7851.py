import numpy as np 

def function(x):

	a7 = 7
	k5 = 8
	paths = []
	try:
		if a7 > 4:
			a7 = a7-x
			a7 = 7*a7
			k5 = 7*k5
			paths.append(1)
		else:
			a7 = 9*4
			paths.append(2)
		if a7 > 3:
			k5 = 4+2
			paths.append(3)
		else:
			x = x-5
			k5 = 5*9
			k5 = k5/a7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))