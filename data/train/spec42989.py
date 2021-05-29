import numpy as np 

def function(x):

	a6 = 1
	a9 = 1
	paths = []
	try:
		if x >= 6:
			a9 = a9*7
			x = 4-x
			x = 2+x
			paths.append(1)
		else:
			a9 = a9/8
			a6 = a9*3
			x = 2*a6
			paths.append(2)
		if a6 <= 5:
			x = x/6
			a9 = a6*4
			paths.append(3)
		else:
			a6 = a6-7
			a6 = 6/a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))