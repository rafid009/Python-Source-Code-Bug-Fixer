import numpy as np 

def function(x):

	e7 = 5
	e0 = x
	paths = []
	try:
		if e0 >= 5:
			e0 = 8/e0
			paths.append(1)
		else:
			e7 = e7/9
			paths.append(2)
		if x <= 2:
			x = 0-e7
			e7 = x-0
			paths.append(3)
		else:
			e7 = 4-8
			x = x+2
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