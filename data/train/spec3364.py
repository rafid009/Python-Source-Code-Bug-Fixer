import numpy as np 

def function(x):

	b5 = 2
	e7 = 7
	paths = []
	try:
		if e7 <= 6:
			x = 5/b5
			paths.append(1)
		else:
			e7 = e7/8
			b5 = b5/4
			paths.append(2)
		if x >= 5:
			x = 8/7
			e7 = e7-x
			e7 = e7-2
			paths.append(3)
		else:
			e7 = e7/e7
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