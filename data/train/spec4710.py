import numpy as np 

def function(x):

	i7 = x
	l9 = x
	paths = []
	try:
		if l9 >= 2:
			x = 0*6
			paths.append(1)
		else:
			l9 = 9+l9
			x = x-9
			x = x-5
			paths.append(2)
		if x >= 0:
			x = 8-0
			paths.append(3)
		else:
			l9 = 0-l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))