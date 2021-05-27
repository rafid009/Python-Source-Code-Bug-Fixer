import numpy as np 

def function(x):

	l8 = 1
	e1 = 8
	paths = []
	try:
		if e1 > 7:
			x = x*4
			x = l8+x
			e1 = 5-1
			paths.append(1)
		else:
			e1 = 0-6
			l8 = l8-l8
			paths.append(2)
		if x > 5:
			x = x*x
			paths.append(3)
		else:
			e1 = l8-2
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