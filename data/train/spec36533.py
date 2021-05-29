import numpy as np 

def function(x):

	l8 = x
	f6 = 3
	paths = []
	try:
		if x <= 8:
			l8 = l8*6
			paths.append(1)
		else:
			x = x/l8
			paths.append(2)
		if x > 8:
			f6 = f6/3
			paths.append(3)
		else:
			x = 1-x
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