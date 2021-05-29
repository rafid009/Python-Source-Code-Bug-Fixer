import numpy as np 

def function(x):

	e5 = 0
	j9 = x
	paths = []
	try:
		if e5 > 3:
			j9 = 1*j9
			e5 = 7-3
			e5 = j9+j9
			paths.append(1)
		else:
			e5 = 9/x
			e5 = 3/j9
			paths.append(2)
		if x >= 3:
			e5 = e5/j9
			paths.append(3)
		else:
			e5 = 1-2
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))