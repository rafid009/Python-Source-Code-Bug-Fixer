import numpy as np 

def function(x):

	l8 = 7
	a3 = 4
	paths = []
	try:
		if l8 >= 1:
			l8 = l8/x
			l8 = l8-4
			a3 = 6*l8
			paths.append(1)
		else:
			a3 = l8/2
			paths.append(2)
		if a3 >= 6:
			x = x/x
			a3 = 7+0
			paths.append(3)
		else:
			l8 = l8*6
			x = x-0
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))