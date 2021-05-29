import numpy as np 

def function(x):

	e7 = 8
	x9 = 8
	paths = []
	try:
		if x < 6:
			e7 = x+4
			x9 = 3/e7
			x9 = 4/x9
			paths.append(1)
		else:
			e7 = 3/e7
			e7 = 2-e7
			paths.append(2)
		if e7 >= 6:
			x9 = x9*5
			x = 7+x
			paths.append(3)
		else:
			x9 = x9+8
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))