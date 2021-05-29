import numpy as np 

def function(x):

	l4 = 0
	a3 = x
	paths = []
	try:
		if a3 > 2:
			x = x-4
			paths.append(1)
		else:
			l4 = 4-x
			paths.append(2)
		if a3 <= 3:
			l4 = l4-3
			paths.append(3)
		else:
			x = 1*x
			l4 = 9+l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))