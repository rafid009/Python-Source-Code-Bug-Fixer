import numpy as np 

def function(x):

	l6 = 3
	l7 = x
	paths = []
	try:
		if x <= 6:
			l7 = x+l7
			l6 = 6*5
			paths.append(1)
		else:
			x = 2-l7
			x = x-8
			paths.append(2)
		if x >= 6:
			l7 = l7/8
			l6 = 6/l6
			l7 = 4-l7
			paths.append(3)
		else:
			l7 = l7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))