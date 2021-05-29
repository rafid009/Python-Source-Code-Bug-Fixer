import numpy as np 

def function(x):

	v7 = x
	e5 = 4
	paths = []
	try:
		if e5 > 5:
			e5 = v7/e5
			x = 0*x
			paths.append(1)
		else:
			x = x/1
			v7 = 3*v7
			x = x/4
			paths.append(2)
		if e5 > 6:
			e5 = x/8
			x = 9*2
			e5 = 5*v7
			paths.append(3)
		else:
			v7 = 8*6
			x = 1-x
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