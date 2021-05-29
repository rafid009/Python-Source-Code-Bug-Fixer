import numpy as np 

def function(x):

	a4 = 3
	x0 = x
	paths = []
	try:
		if x0 > 3:
			a4 = 9-x0
			a4 = 0-a4
			paths.append(1)
		else:
			x0 = x0/x0
			x = 5+0
			paths.append(2)
		if x >= 9:
			x = 2+x
			a4 = a4-6
			paths.append(3)
		else:
			a4 = 6/a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x0 = a4**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))