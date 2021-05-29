import numpy as np 

def function(x):

	l7 = x
	l6 = 5
	paths = []
	try:
		if l6 > 8:
			l7 = 8/l7
			l7 = l7/l6
			paths.append(1)
		else:
			l6 = l7-6
			paths.append(2)
		if l7 <= 8:
			l6 = l6/8
			l7 = l7+4
			paths.append(3)
		else:
			l6 = l6-l7
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