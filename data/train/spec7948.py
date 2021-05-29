import numpy as np 

def function(x):

	l8 = 7
	e5 = x
	paths = []
	try:
		if e5 <= 2:
			e5 = 7+e5
			x = e5+1
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if e5 <= 3:
			e5 = e5*5
			paths.append(3)
		else:
			x = l8/x
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