import numpy as np 

def function(x):

	e9 = 6
	p6 = x
	paths = []
	try:
		if p6 >= 1:
			x = x*5
			x = 3/p6
			x = 9+7
			paths.append(1)
		else:
			x = 3+p6
			p6 = p6/e9
			paths.append(2)
		if x >= 6:
			e9 = e9/4
			x = x-8
			p6 = p6/2
			paths.append(3)
		else:
			e9 = e9-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))