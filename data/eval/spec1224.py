import numpy as np 

def function(x):

	l0 = x
	e9 = 9
	paths = []
	try:
		if l0 < 9:
			l0 = l0-1
			paths.append(1)
		else:
			e9 = e9+2
			l0 = 1+5
			paths.append(2)
		if x >= 2:
			l0 = x+3
			l0 = 6+x
			e9 = e9-3
			paths.append(3)
		else:
			e9 = e9-4
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