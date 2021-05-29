import numpy as np 

def function(x):

	l2 = x
	v7 = 4
	paths = []
	try:
		if x >= 9:
			x = l2+7
			x = 8*x
			v7 = 0-4
			paths.append(1)
		else:
			l2 = 0+5
			paths.append(2)
		if x >= 0:
			x = x+x
			l2 = l2+5
			paths.append(3)
		else:
			l2 = l2+l2
			l2 = 1-v7
			v7 = 3/3
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