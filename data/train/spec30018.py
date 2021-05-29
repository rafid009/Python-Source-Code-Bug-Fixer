import numpy as np 

def function(x):

	x5 = 7
	a9 = 8
	x = x
	paths = []
	try:
		if x >= 9:
			a9 = 9-a9
			a9 = a9-7
			paths.append(1)
		else:
			a9 = x5-1
			x = x*5
			paths.append(2)
		if a9 >= 9:
			x = 6*x
			paths.append(3)
		else:
			x5 = 2-9
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		a9 = x5**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))