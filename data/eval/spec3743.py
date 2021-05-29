import numpy as np 

def function(x):

	e4 = 6
	l5 = 2
	paths = []
	try:
		if e4 < 6:
			l5 = 7*l5
			paths.append(1)
		else:
			e4 = e4/e4
			paths.append(2)
		if l5 < 1:
			x = 5+x
			l5 = 5*l5
			l5 = l5/8
			paths.append(3)
		else:
			l5 = 0+l5
			l5 = 6*l5
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