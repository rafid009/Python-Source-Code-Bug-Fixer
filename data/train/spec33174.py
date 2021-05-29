import numpy as np 

def function(x):

	l2 = 6
	x3 = x
	paths = []
	try:
		if l2 >= 8:
			x = 3*x3
			x3 = 3+7
			paths.append(1)
		else:
			l2 = l2/3
			l2 = 3*l2
			x3 = x3/l2
			paths.append(2)
		if x > 1:
			x3 = 9+9
			x3 = x-7
			paths.append(3)
		else:
			l2 = x3-l2
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