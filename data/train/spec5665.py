import numpy as np 

def function(x):

	e0 = 1
	e7 = 7
	paths = []
	try:
		if e7 <= 7:
			e0 = e0+7
			x = 1*x
			paths.append(1)
		else:
			e7 = e7*9
			paths.append(2)
		if e0 > 5:
			e0 = 4+1
			paths.append(3)
		else:
			e7 = x*e7
			x = 2+x
			e0 = 9-e0
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