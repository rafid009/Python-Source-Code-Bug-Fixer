import numpy as np 

def function(x):

	e4 = 1
	l6 = x
	paths = []
	try:
		if e4 <= 1:
			e4 = 9+e4
			paths.append(1)
		else:
			l6 = l6*e4
			l6 = 5/e4
			x = 8/x
			paths.append(2)
		if e4 <= 6:
			l6 = 8+l6
			x = x/e4
			paths.append(3)
		else:
			e4 = e4*6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))