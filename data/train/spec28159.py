import numpy as np 

def function(x):

	b7 = 9
	a8 = 8
	paths = []
	try:
		if a8 > 6:
			a8 = 6*5
			b7 = 2/b7
			paths.append(1)
		else:
			x = 4*a8
			a8 = 7/x
			paths.append(2)
		if b7 >= 5:
			x = 0+6
			b7 = 6-2
			x = 5/x
			paths.append(3)
		else:
			b7 = b7/6
			b7 = 2/x
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