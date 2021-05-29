import numpy as np 

def function(x):

	i1 = x
	e2 = 5
	paths = []
	try:
		if e2 <= 6:
			i1 = i1/4
			i1 = 3/i1
			e2 = e2-9
			paths.append(1)
		else:
			x = i1-e2
			e2 = 7*e2
			paths.append(2)
		if x <= 5:
			i1 = i1-9
			paths.append(3)
		else:
			e2 = 2*e2
			e2 = 1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))