import numpy as np 

def function(x):

	x9 = x
	e8 = 2
	paths = []
	try:
		if x >= 0:
			x = 4-x
			e8 = e8*3
			e8 = e8+1
			paths.append(1)
		else:
			x = x-7
			x9 = x*e8
			e8 = e8-0
			paths.append(2)
		if x <= 1:
			x9 = e8+4
			paths.append(3)
		else:
			e8 = 3*e8
			x = x/6
			x9 = 5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))