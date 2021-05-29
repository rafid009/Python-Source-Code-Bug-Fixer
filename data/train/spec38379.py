import numpy as np 

def function(x):

	v6 = 7
	a8 = 5
	paths = []
	try:
		if v6 > 9:
			v6 = 5+v6
			paths.append(1)
		else:
			a8 = a8*a8
			x = 7-x
			paths.append(2)
		if a8 >= 0:
			a8 = 0*a8
			x = 2/x
			paths.append(3)
		else:
			x = 7*x
			x = 1-v6
			a8 = a8+7
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