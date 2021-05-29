import numpy as np 

def function(x):

	e3 = 6
	y8 = x
	paths = []
	try:
		if e3 <= 7:
			x = x/9
			paths.append(1)
		else:
			x = 1-y8
			e3 = e3*y8
			e3 = 4+e3
			paths.append(2)
		if y8 >= 2:
			e3 = e3*y8
			y8 = y8/x
			paths.append(3)
		else:
			x = 0-9
			y8 = 6/y8
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		e3 = y8**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))