import numpy as np 

def function(x):

	e3 = 9
	e4 = 1
	paths = []
	try:
		if x >= 5:
			e4 = e4/e3
			e4 = e4*5
			e4 = 2/e3
			paths.append(1)
		else:
			e4 = e4*9
			paths.append(2)
		if e4 < 4:
			x = 1*x
			paths.append(3)
		else:
			e3 = e3*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))