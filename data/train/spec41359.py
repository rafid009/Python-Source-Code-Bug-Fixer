import numpy as np 

def function(x):

	d7 = 9
	e1 = 3
	paths = []
	try:
		if e1 > 1:
			d7 = d7/4
			d7 = d7+x
			paths.append(1)
		else:
			e1 = d7/x
			x = d7-6
			x = 1-x
			paths.append(2)
		if x >= 6:
			x = 7/3
			paths.append(3)
		else:
			d7 = 5*x
			d7 = 1*x
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