import numpy as np 

def function(x):

	e7 = x
	a6 = x
	paths = []
	try:
		if e7 > 0:
			x = x*6
			paths.append(1)
		else:
			e7 = 4-e7
			e7 = 5-e7
			e7 = e7*x
			paths.append(2)
		if a6 > 1:
			e7 = a6/4
			a6 = a6*3
			x = 2/e7
			paths.append(3)
		else:
			a6 = 3/a6
			x = x*4
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))