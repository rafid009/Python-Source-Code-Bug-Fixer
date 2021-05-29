import numpy as np 

def function(x):

	j0 = 3
	l6 = 6
	paths = []
	try:
		if j0 < 0:
			x = 9/9
			l6 = 8-2
			paths.append(1)
		else:
			j0 = j0+7
			j0 = 9*j0
			l6 = 5/l6
			paths.append(2)
		if x < 8:
			x = l6-2
			paths.append(3)
		else:
			j0 = j0/j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))