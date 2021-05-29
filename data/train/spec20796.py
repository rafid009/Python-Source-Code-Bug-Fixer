import numpy as np 

def function(x):

	x1 = 0
	e7 = 6
	paths = []
	try:
		if e7 > 8:
			e7 = e7-x
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if e7 >= 4:
			x = x+5
			x = 2*x
			paths.append(3)
		else:
			x = 6+x
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))