import numpy as np 

def function(x):

	l7 = 3
	d8 = x
	paths = []
	try:
		if l7 <= 7:
			x = x-x
			paths.append(1)
		else:
			l7 = l7+x
			paths.append(2)
		if l7 > 0:
			x = 3-d8
			paths.append(3)
		else:
			l7 = x-l7
			x = 3/x
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