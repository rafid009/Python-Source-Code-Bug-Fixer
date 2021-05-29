import numpy as np 

def function(x):

	a2 = 2
	e5 = x
	paths = []
	try:
		if e5 >= 2:
			x = a2*8
			e5 = e5*5
			a2 = 1-9
			paths.append(1)
		else:
			a2 = a2-1
			x = 1/5
			a2 = a2/3
			paths.append(2)
		if a2 > 3:
			a2 = e5/a2
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))