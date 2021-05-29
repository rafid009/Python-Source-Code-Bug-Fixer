import numpy as np 

def function(x):

	a6 = x
	p2 = x
	paths = []
	try:
		if a6 >= 4:
			p2 = p2-3
			paths.append(1)
		else:
			x = a6/p2
			paths.append(2)
		if a6 > 6:
			a6 = 4/a6
			a6 = 5+a6
			x = 5-x
			paths.append(3)
		else:
			x = 9-x
			a6 = 9+a6
			x = x-9
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