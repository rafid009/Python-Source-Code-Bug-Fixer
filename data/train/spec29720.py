import numpy as np 

def function(x):

	o7 = x
	e7 = x
	paths = []
	try:
		if x >= 7:
			x = x/5
			paths.append(1)
		else:
			x = o7/x
			o7 = o7-4
			paths.append(2)
		if x <= 8:
			x = 6/3
			paths.append(3)
		else:
			e7 = 0*e7
			x = x-o7
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		e7 = o7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))