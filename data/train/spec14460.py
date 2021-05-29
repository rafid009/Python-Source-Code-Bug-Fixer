import numpy as np 

def function(x):

	l6 = x
	l5 = 7
	paths = []
	try:
		if l6 < 0:
			l6 = x-7
			l6 = l5-l6
			paths.append(1)
		else:
			l6 = x/l5
			paths.append(2)
		if x >= 1:
			l5 = 7-l5
			x = l5*x
			paths.append(3)
		else:
			x = x-1
			l6 = 9-l6
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