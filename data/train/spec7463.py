import numpy as np 

def function(x):

	x0 = 1
	a4 = 9
	paths = []
	try:
		if a4 > 6:
			x0 = 6+x0
			x = x0-x
			paths.append(1)
		else:
			a4 = a4/7
			paths.append(2)
		if x0 >= 8:
			x = x/a4
			x0 = x0-a4
			paths.append(3)
		else:
			a4 = a4-9
			x0 = x0+x
			x0 = x-x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		a4 = x0**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))