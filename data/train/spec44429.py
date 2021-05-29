import numpy as np 

def function(x):

	e7 = 1
	a5 = 0
	paths = []
	try:
		if x >= 7:
			e7 = a5+1
			paths.append(1)
		else:
			e7 = a5/x
			e7 = 8*2
			e7 = 3/e7
			paths.append(2)
		if x >= 7:
			e7 = 0/4
			a5 = 2*4
			e7 = x+e7
			paths.append(3)
		else:
			a5 = a5/1
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