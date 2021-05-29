import numpy as np 

def function(x):

	e7 = 1
	u0 = x
	paths = []
	try:
		if u0 > 3:
			e7 = e7+x
			u0 = u0+3
			paths.append(1)
		else:
			e7 = e7*3
			e7 = u0-1
			u0 = 5-u0
			paths.append(2)
		if e7 < 3:
			e7 = u0+6
			e7 = x*e7
			paths.append(3)
		else:
			e7 = e7-9
			e7 = e7*9
			e7 = u0*6
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