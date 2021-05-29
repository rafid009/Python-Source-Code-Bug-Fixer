import numpy as np 

def function(x):

	n0 = 5
	l7 = 6
	paths = []
	try:
		if x >= 5:
			l7 = 4*x
			l7 = l7-7
			paths.append(1)
		else:
			n0 = n0/n0
			paths.append(2)
		if l7 <= 2:
			l7 = 6/4
			n0 = n0/n0
			paths.append(3)
		else:
			n0 = 7-6
			l7 = l7+l7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))