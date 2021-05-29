import numpy as np 

def function(x):

	a8 = 0
	b7 = 1
	paths = []
	try:
		if b7 <= 1:
			b7 = b7-2
			paths.append(1)
		else:
			a8 = 6-x
			b7 = a8-2
			paths.append(2)
		if b7 > 2:
			a8 = a8-4
			a8 = 5/a8
			x = x-0
			paths.append(3)
		else:
			b7 = 4-8
			x = 3-x
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