import numpy as np 

def function(x):

	l0 = x
	n5 = x
	paths = []
	try:
		if x <= 0:
			l0 = l0-8
			x = 4/x
			l0 = l0-6
			paths.append(1)
		else:
			n5 = 9+9
			paths.append(2)
		if n5 > 6:
			n5 = x-2
			x = 0-1
			paths.append(3)
		else:
			n5 = n5/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))