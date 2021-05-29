import numpy as np 

def function(x):

	l0 = 5
	i9 = x
	paths = []
	try:
		if x < 1:
			l0 = i9/i9
			paths.append(1)
		else:
			x = 5*i9
			i9 = x-l0
			paths.append(2)
		if x <= 1:
			i9 = i9-x
			l0 = l0-l0
			paths.append(3)
		else:
			l0 = l0+2
			i9 = i9/6
			x = 8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))