import numpy as np 

def function(x):

	l9 = x
	e4 = 0
	paths = []
	try:
		if e4 < 4:
			x = x-3
			l9 = l9-e4
			e4 = x-l9
			paths.append(1)
		else:
			l9 = 5+l9
			paths.append(2)
		if x > 1:
			e4 = l9/e4
			e4 = x-4
			paths.append(3)
		else:
			e4 = 6-e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))