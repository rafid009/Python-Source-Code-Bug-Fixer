import numpy as np 

def function(x):

	l6 = x
	l7 = 2
	paths = []
	try:
		if x >= 8:
			l6 = 8-l6
			paths.append(1)
		else:
			l7 = l7-8
			x = l6/x
			paths.append(2)
		if x <= 8:
			l7 = l7-5
			paths.append(3)
		else:
			x = x*l6
			l6 = l6-2
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))