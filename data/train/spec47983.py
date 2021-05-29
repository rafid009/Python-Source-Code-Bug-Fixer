import numpy as np 

def function(x):

	e2 = 5
	l9 = 4
	paths = []
	try:
		if e2 < 3:
			l9 = l9*l9
			paths.append(1)
		else:
			x = 1-x
			l9 = 6+l9
			x = 6/x
			paths.append(2)
		if e2 < 3:
			x = e2-l9
			e2 = e2*x
			paths.append(3)
		else:
			l9 = 7*4
			e2 = x/7
			l9 = 4+l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))