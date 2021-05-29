import numpy as np 

def function(x):

	a8 = 2
	f1 = 6
	paths = []
	try:
		if x >= 3:
			x = a8-x
			x = 7+a8
			paths.append(1)
		else:
			a8 = 3-a8
			x = 2-9
			paths.append(2)
		if x >= 6:
			a8 = x/5
			a8 = a8+2
			paths.append(3)
		else:
			a8 = a8/1
			a8 = f1-a8
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