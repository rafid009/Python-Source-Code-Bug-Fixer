import numpy as np 

def function(x):

	e3 = x
	x5 = 3
	paths = []
	try:
		if e3 <= 4:
			e3 = e3+5
			x5 = x5/5
			x5 = e3+7
			paths.append(1)
		else:
			e3 = 9*5
			paths.append(2)
		if x5 <= 1:
			x5 = 7*9
			paths.append(3)
		else:
			e3 = e3*e3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))