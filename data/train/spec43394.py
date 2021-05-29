import numpy as np 

def function(x):

	a7 = x
	a4 = 8
	paths = []
	try:
		if a7 < 0:
			a7 = 6*a7
			a7 = 4+a7
			a7 = 4-a4
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if a4 >= 1:
			x = a4/x
			a7 = x+a4
			a7 = a7*6
			paths.append(3)
		else:
			x = a7-3
			a7 = a4/a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))