import numpy as np 

def function(x):

	l2 = x
	a9 = 6
	paths = []
	try:
		if a9 < 2:
			l2 = l2/l2
			paths.append(1)
		else:
			a9 = a9-5
			l2 = l2/6
			a9 = a9+x
			paths.append(2)
		if a9 > 3:
			x = a9/6
			paths.append(3)
		else:
			x = x+7
			a9 = 8/a9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))