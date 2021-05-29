import numpy as np 

def function(x):

	l2 = 6
	m6 = x
	x = 2
	paths = []
	try:
		if x < 1:
			x = 3/3
			paths.append(1)
		else:
			x = l2/x
			l2 = m6+l2
			paths.append(2)
		if x < 3:
			l2 = 3/l2
			paths.append(3)
		else:
			l2 = 3/7
			x = m6-6
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