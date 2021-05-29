import numpy as np 

def function(x):

	e2 = 8
	a4 = 5
	paths = []
	try:
		if x >= 0:
			e2 = 0+1
			x = x+5
			paths.append(1)
		else:
			a4 = 0-a4
			paths.append(2)
		if e2 > 2:
			e2 = e2+9
			paths.append(3)
		else:
			e2 = 4-e2
			a4 = 0*a4
			a4 = a4+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))