import numpy as np 

def function(x):

	e8 = x
	e0 = 0
	paths = []
	try:
		if e0 < 6:
			e0 = x+4
			e0 = 7-x
			paths.append(1)
		else:
			e0 = 9+e0
			paths.append(2)
		if e8 < 7:
			e8 = 1*e8
			paths.append(3)
		else:
			e0 = 1/5
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))