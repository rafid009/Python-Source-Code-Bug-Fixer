import numpy as np 

def function(x):

	e1 = 7
	a2 = x
	paths = []
	try:
		if x >= 5:
			e1 = 1/6
			x = x-6
			a2 = 3-4
			paths.append(1)
		else:
			a2 = 4*4
			e1 = 9*1
			x = 9*x
			paths.append(2)
		if x < 9:
			e1 = 1+e1
			a2 = a2/7
			paths.append(3)
		else:
			e1 = x+e1
			x = 8*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))