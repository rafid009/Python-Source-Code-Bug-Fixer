import numpy as np 

def function(x):

	e4 = 8
	x5 = 6
	paths = []
	try:
		if x > 3:
			e4 = 2/e4
			e4 = e4*1
			x = x*x5
			paths.append(1)
		else:
			x5 = x5/x5
			x5 = 3+x
			e4 = e4-0
			paths.append(2)
		if e4 > 3:
			e4 = e4/6
			x = 2-x
			x = x-4
			paths.append(3)
		else:
			e4 = e4/e4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))