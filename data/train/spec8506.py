import numpy as np 

def function(x):

	e8 = x
	v7 = x
	paths = []
	try:
		if e8 >= 3:
			e8 = 7*x
			v7 = v7/2
			paths.append(1)
		else:
			e8 = e8-x
			paths.append(2)
		if e8 <= 8:
			e8 = 5/5
			e8 = 7-e8
			paths.append(3)
		else:
			e8 = 6-5
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