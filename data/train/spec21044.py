import numpy as np 

def function(x):

	a9 = 4
	e8 = 0
	paths = []
	try:
		if a9 < 3:
			a9 = a9-4
			a9 = e8/x
			paths.append(1)
		else:
			a9 = 9*a9
			a9 = 2*8
			paths.append(2)
		if a9 > 0:
			a9 = a9*1
			e8 = e8-1
			x = x/x
			paths.append(3)
		else:
			a9 = a9-3
			e8 = 2*e8
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