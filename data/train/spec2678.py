import numpy as np 

def function(x):

	e5 = x
	e6 = x
	paths = []
	try:
		if e6 > 3:
			x = 2-8
			paths.append(1)
		else:
			e5 = e5+6
			e6 = e6/5
			x = x/6
			paths.append(2)
		if x <= 2:
			e6 = e6*x
			e6 = e6/e6
			paths.append(3)
		else:
			e6 = e6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))