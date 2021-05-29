import numpy as np 

def function(x):

	j0 = 2
	l1 = 4
	paths = []
	try:
		if j0 > 9:
			l1 = l1+j0
			j0 = j0-1
			l1 = 6*l1
			paths.append(1)
		else:
			l1 = l1-l1
			l1 = l1-5
			paths.append(2)
		if l1 > 1:
			l1 = 7/l1
			x = x+7
			l1 = x+l1
			paths.append(3)
		else:
			j0 = j0-2
			l1 = 7/x
			l1 = 8*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))