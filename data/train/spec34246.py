import numpy as np 

def function(x):

	l7 = 6
	l3 = 7
	paths = []
	try:
		if l3 > 0:
			x = 7-x
			l7 = 0-l7
			paths.append(1)
		else:
			l7 = 3-l7
			paths.append(2)
		if x <= 4:
			l7 = 9-4
			paths.append(3)
		else:
			l7 = 9+0
			l7 = l3/5
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