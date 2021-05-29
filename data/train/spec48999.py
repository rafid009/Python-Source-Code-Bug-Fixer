import numpy as np 

def function(x):

	l8 = 8
	x7 = 9
	x = x
	paths = []
	try:
		if x >= 7:
			l8 = l8/7
			x = x*x7
			x = 9/3
			paths.append(1)
		else:
			l8 = l8/7
			paths.append(2)
		if x < 0:
			x7 = 5-l8
			l8 = 3*l8
			x = 5-x
			paths.append(3)
		else:
			l8 = l8+x
			x = 0-l8
			x7 = 5/x7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))