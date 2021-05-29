import numpy as np 

def function(x):

	x6 = x
	e8 = x
	paths = []
	try:
		if e8 < 3:
			x = 7*x
			x = x-9
			x6 = 7*e8
			paths.append(1)
		else:
			x = x+x
			x6 = 3-2
			paths.append(2)
		if e8 >= 2:
			x = e8/x
			paths.append(3)
		else:
			e8 = 3-7
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		e8 = x6**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))