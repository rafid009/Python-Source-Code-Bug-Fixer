import numpy as np 

def function(x):

	e5 = 7
	a5 = 0
	x = x
	paths = []
	try:
		if a5 >= 9:
			a5 = 7-a5
			x = 1+6
			paths.append(1)
		else:
			x = x+e5
			a5 = 1+4
			paths.append(2)
		if e5 > 2:
			e5 = e5+5
			paths.append(3)
		else:
			a5 = 4+1
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