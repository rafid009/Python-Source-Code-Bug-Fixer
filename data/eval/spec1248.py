import numpy as np 

def function(x):

	l4 = x
	e8 = x
	paths = []
	try:
		if e8 < 8:
			e8 = e8/9
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x > 1:
			e8 = 5+e8
			paths.append(3)
		else:
			l4 = l4+3
			l4 = 3/3
			e8 = e8/9
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