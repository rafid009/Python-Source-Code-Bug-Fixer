import numpy as np 

def function(x):

	e5 = x
	l5 = x
	paths = []
	try:
		if e5 > 8:
			l5 = 9*l5
			e5 = 1-e5
			paths.append(1)
		else:
			e5 = 5-4
			paths.append(2)
		if x > 0:
			l5 = x-9
			paths.append(3)
		else:
			e5 = x+l5
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		e5 = l5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))