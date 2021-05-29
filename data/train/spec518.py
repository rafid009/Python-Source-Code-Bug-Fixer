import numpy as np 

def function(x):

	k7 = x
	e7 = 7
	paths = []
	try:
		if k7 >= 6:
			x = e7-1
			k7 = k7+6
			e7 = 3/e7
			paths.append(1)
		else:
			x = x-5
			k7 = k7+7
			paths.append(2)
		if k7 <= 3:
			e7 = e7*5
			paths.append(3)
		else:
			e7 = x/e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))