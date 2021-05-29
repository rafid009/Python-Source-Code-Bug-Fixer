import numpy as np 

def function(x):

	l8 = 5
	e1 = x
	paths = []
	try:
		if e1 < 4:
			e1 = e1/3
			e1 = e1*6
			paths.append(1)
		else:
			l8 = 7-e1
			l8 = 2*x
			paths.append(2)
		if x < 8:
			e1 = e1+8
			paths.append(3)
		else:
			e1 = e1*3
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